#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ランチ営業ライブ配信（定点2時間）から、ショート／リール用の縦動画を自動で切り抜くツール。

音の盛り上がり（会話・笑い声・調理音）と画面の動き（お客さんの出入り・配膳）を解析して、
「にぎわっている場面」を自動で見つけ、9:16の縦動画に書き出します。

使い方:
    python3 clip.py 動画ファイル.mp4
    python3 clip.py 動画ファイル.mp4 --count 8 --length 30
"""

import argparse
import csv
import os
import re
import shutil
import subprocess
import sys
import tempfile

# ---------------------------------------------------------------- ffmpeg 探索


def find_tool(name):
    """システムの ffmpeg/ffprobe を探し、無ければ imageio-ffmpeg 同梱版を使う。"""
    found = shutil.which(name)
    if found:
        return found
    if name == "ffmpeg":
        try:
            import imageio_ffmpeg

            return imageio_ffmpeg.get_ffmpeg_exe()
        except Exception:
            pass
    return None


FFMPEG = find_tool("ffmpeg")
FFPROBE = find_tool("ffprobe")

if not FFMPEG:
    sys.exit(
        "ffmpeg が見つかりません。次のコマンドで入れてください:\n"
        "    pip3 install imageio-ffmpeg\n"
        "  （または  brew install ffmpeg ）"
    )


def run(cmd):
    """ffmpeg を実行し、標準出力＋標準エラーをまとめて返す。"""
    p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, errors="replace")
    return p.stdout


# ---------------------------------------------------------------- 動画の情報


def probe_duration(path):
    """動画の長さ（秒）を取得する。ffprobe が無ければ ffmpeg のログから拾う。"""
    if FFPROBE:
        out = run([FFPROBE, "-v", "error", "-show_entries", "format=duration",
                   "-of", "default=nw=1:nk=1", path]).strip()
        try:
            return float(out.splitlines()[-1])
        except (ValueError, IndexError):
            pass
    out = run([FFMPEG, "-i", path])
    m = re.search(r"Duration:\s*(\d+):(\d+):(\d+\.?\d*)", out)
    if not m:
        sys.exit("動画の長さを取得できませんでした: " + path)
    h, mnt, s = m.groups()
    return int(h) * 3600 + int(mnt) * 60 + float(s)


def has_audio(path):
    if FFPROBE:
        out = run([FFPROBE, "-v", "error", "-select_streams", "a",
                   "-show_entries", "stream=index", "-of", "csv=p=0", path]).strip()
        return bool(out)
    return "Audio:" in run([FFMPEG, "-i", path])


# ---------------------------------------------------------------- 解析


def _parse_metadata_file(path, key_pattern):
    """ffmpeg の metadata=print が書いた解析ファイルを {秒: 値} に変換する。"""
    values = {}
    t = None
    with open(path, "r", errors="replace") as fh:
        for line in fh:
            m = re.search(r"pts_time:(-?[\d.]+)", line)
            if m:
                t = float(m.group(1))
                continue
            m = re.search(key_pattern, line)
            if m and t is not None:
                raw = m.group(1)
                try:
                    values[t] = float(raw)
                except ValueError:
                    values[t] = float("-inf") if raw.lstrip("-").startswith("inf") else 0.0
    return values


def _analyze(path, out_flag, filter_args, key_pattern):
    with tempfile.NamedTemporaryFile(suffix=".txt", delete=False) as f:
        meta = f.name
    try:
        run([FFMPEG, "-hide_banner", "-nostats", out_flag, "-i", path]
            + filter_args(meta) + ["-f", "null", "-"])
        return _parse_metadata_file(meta, key_pattern)
    finally:
        if os.path.exists(meta):
            os.remove(meta)


def analyze_audio(path, duration):
    """1秒ごとの音量(dB)を測る。にぎわい・会話・笑い声の指標。

    ebur128 のログは環境によって出力されないため、1秒ぶんのフレームに切り直して
    astats で RMS を取る方式にしている（確実にファイルへ書き出される）。
    """
    SILENT = -91.0
    values = _analyze(
        path, "-vn",
        lambda meta: ["-af", "asetnsamples=n=48000,astats=metadata=1:reset=1,"
                             "ametadata=print:key=lavfi.astats.Overall.RMS_level:"
                             "file=" + meta],
        r"RMS_level=(-?[\w.]+)")
    bins = [SILENT] * (int(duration) + 1)
    for t, v in values.items():
        i = int(t)
        if 0 <= i < len(bins):
            level = SILENT if v == float("-inf") else max(v, SILENT)
            bins[i] = max(bins[i], level)
    return bins


def analyze_motion(path, duration):
    """1秒ごとの画面の動き量を測る。

    定点カメラでは「場面転換(scene score)」はまったく反応しないため、
    連続フレームの差分の大きさ（＝人の出入り・配膳・手の動き）を使う。
    """
    values = _analyze(
        path, "-an",
        lambda meta: ["-vf", "fps=2,scale=320:-2,format=gray,"
                             "tblend=all_mode=difference,signalstats,"
                             "metadata=print:key=lavfi.signalstats.YAVG:"
                             "file=" + meta],
        r"YAVG=([\d.]+)")
    bins = [0.0] * (int(duration) + 1)
    for t, v in values.items():
        # 先頭フレームは差分の相手がおらず異常値になるため捨てる
        if t < 1.0:
            continue
        i = int(t)
        if 0 <= i < len(bins):
            bins[i] += v
    return bins


def normalize(values):
    """0〜1に正規化する。一瞬の外れ値に潰されないよう上下5%は切り捨てる。"""
    ordered = sorted(values)
    n = len(ordered)
    lo = ordered[int(n * 0.05)]
    hi = ordered[min(n - 1, int(n * 0.95))]
    if hi - lo < 1e-9:
        lo, hi = min(values), max(values)
    if hi - lo < 1e-9:
        return [0.0] * n
    return [min(1.0, max(0.0, (v - lo) / (hi - lo))) for v in values]


# ---------------------------------------------------------------- 見どころ選定


def pick_highlights(score, length, count, skip_head, skip_tail, gap):
    """スコアの高い区間を、重ならないように上位から選ぶ。"""
    n = len(score)
    end_limit = n - skip_tail - length
    if end_limit <= skip_head:
        skip_head, end_limit = 0, max(0, n - length)

    # 各開始秒について、その先 length 秒の平均スコアを出す
    window = []
    running = sum(score[skip_head:skip_head + length])
    for start in range(skip_head, end_limit + 1):
        if start > skip_head:
            running += score[start + length - 1] - score[start - 1]
        window.append((running / length, start))

    window.sort(reverse=True)
    picked = []
    for avg, start in window:
        if len(picked) >= count:
            break
        if all(abs(start - p) >= length + gap for _, p in picked):
            picked.append((avg, start))
    picked.sort(key=lambda x: x[1])
    return picked


# ---------------------------------------------------------------- 書き出し


def build_filter(style, crop_x, fps):
    """9:16（1080x1920）の縦動画にする映像フィルタを組み立てる。"""
    if style == "blur":
        # 横位置を変えず全体を写し、上下の余白を「ぼかした背景」で埋める
        return (
            "split=2[bg][fg];"
            "[bg]scale=1080:1920:force_original_aspect_ratio=increase,"
            "crop=1080:1920,gblur=sigma=25[bgb];"
            "[fg]scale=1080:-2[fgs];"
            "[bgb][fgs]overlay=(W-w)/2:(H-h)/2,"
            "fps={fps},setsar=1,format=yuv420p".format(fps=fps)
        )
    # crop: 画面の一部を切り出して画面いっぱいの縦動画にする（迫力が出る既定の方式）
    # 幅は偶数に丸める（奇数だと ffmpeg が SAR を補正して縦横比がずれるため）
    return (
        "crop=w='2*floor(min(iw,ih*9/16)/2)':h='2*floor(ih/2)':"
        "x='(iw-2*floor(min(iw,ih*9/16)/2))*{cx}':y=0,"
        "scale=1080:1920:flags=lanczos,fps={fps},setsar=1,format=yuv420p"
    ).format(cx=crop_x, fps=fps)


def cut(src, start, length, out_path, style, crop_x, fps, audio, preset):
    vf = build_filter(style, crop_x, fps)
    cmd = [FFMPEG, "-hide_banner", "-nostats", "-y",
           "-ss", "{:.2f}".format(start), "-i", src, "-t", str(length)]
    cmd += ["-filter_complex" if style == "blur" else "-vf", vf]
    cmd += ["-c:v", "libx264", "-preset", preset, "-crf", "20",
            "-profile:v", "high", "-level", "4.0", "-g", str(fps * 2)]
    if audio:
        cmd += ["-c:a", "aac", "-b:a", "128k", "-ar", "48000", "-ac", "2"]
    else:
        cmd += ["-an"]
    cmd += ["-movflags", "+faststart", out_path]
    out = run(cmd)
    if not os.path.exists(out_path) or os.path.getsize(out_path) == 0:
        print(out[-1500:], file=sys.stderr)
        raise RuntimeError("書き出しに失敗しました: " + out_path)


def hhmmss(seconds):
    s = int(seconds)
    return "{:02d}:{:02d}:{:02d}".format(s // 3600, (s % 3600) // 60, s % 60)


# ---------------------------------------------------------------- メイン


def main():
    ap = argparse.ArgumentParser(
        description="ライブ配信の定点動画から、ショート／リール用の縦動画を自動で切り抜きます。")
    ap.add_argument("input", help="元の動画ファイル")
    ap.add_argument("-o", "--outdir", default="clips", help="書き出し先フォルダ（既定: clips）")
    ap.add_argument("-n", "--count", type=int, default=6, help="切り抜く本数（既定: 6）")
    ap.add_argument("-l", "--length", type=int, default=30, help="1本の長さ・秒（既定: 30）")
    ap.add_argument("--style", choices=["crop", "blur"], default="crop",
                    help="crop=画面を切り出して迫力重視 / blur=全体を写し余白をぼかす")
    ap.add_argument("--crop-x", type=float, default=0.5,
                    help="切り出す横位置 0.0=左端 0.5=中央 1.0=右端（既定: 0.5）")
    ap.add_argument("--fps", type=int, default=30, help="書き出しfps（既定: 30）")
    ap.add_argument("--preset", default="medium",
                    choices=["ultrafast", "superfast", "veryfast", "faster",
                             "fast", "medium", "slow"],
                    help="書き出し速度。スマホでは veryfast 推奨（既定: medium）")
    ap.add_argument("--skip-head", type=int, default=60, help="冒頭の除外秒数（既定: 60）")
    ap.add_argument("--skip-tail", type=int, default=60, help="末尾の除外秒数（既定: 60）")
    ap.add_argument("--gap", type=int, default=60, help="切り抜き同士の最低間隔・秒（既定: 60）")
    ap.add_argument("--dry-run", action="store_true", help="切り出さず候補の時刻だけ表示")
    args = ap.parse_args()

    if not os.path.exists(args.input):
        sys.exit("ファイルが見つかりません: " + args.input)

    duration = probe_duration(args.input)
    audio = has_audio(args.input)
    print("■ 元動画: {}  長さ {}".format(os.path.basename(args.input), hhmmss(duration)))

    if duration < args.length + 5:
        sys.exit("動画が短すぎます（切り抜き長 {} 秒に対して {} 秒）".format(args.length, int(duration)))

    # 短い動画では冒頭・末尾の除外や間隔を自動で緩める
    if duration < 600:
        args.skip_head = min(args.skip_head, int(duration * 0.05))
        args.skip_tail = min(args.skip_tail, int(duration * 0.05))
        args.gap = min(args.gap, max(1, int(args.length / 3)))

    print("■ 解析中… （音の盛り上がりと画面の動きを調べます）")
    motion = normalize(analyze_motion(args.input, duration))
    if audio:
        loud = normalize(analyze_audio(args.input, duration))
        score = [0.6 * a + 0.4 * m for a, m in zip(loud, motion)]
    else:
        print("  （音声トラックが無いため、画面の動きだけで判定します）")
        score = motion

    picked = pick_highlights(score, args.length, args.count,
                             args.skip_head, args.skip_tail, args.gap)
    if not picked:
        sys.exit("見どころを検出できませんでした。--length を短くしてお試しください。")

    print("■ 見どころ候補 {} 件".format(len(picked)))
    for i, (avg, start) in enumerate(picked, 1):
        print("   {:2d}. {} 〜 {}   スコア {:.3f}".format(
            i, hhmmss(start), hhmmss(start + args.length), avg))

    if args.dry_run:
        return

    os.makedirs(args.outdir, exist_ok=True)
    rows = []
    for i, (avg, start) in enumerate(picked, 1):
        name = "clip{:02d}_{}.mp4".format(i, hhmmss(start).replace(":", ""))
        out_path = os.path.join(args.outdir, name)
        print("■ 書き出し {}/{}  {}".format(i, len(picked), name))
        cut(args.input, start, args.length, out_path,
            args.style, args.crop_x, args.fps, audio, args.preset)
        rows.append({
            "ファイル名": name,
            "開始": hhmmss(start),
            "終了": hhmmss(start + args.length),
            "長さ(秒)": args.length,
            "スコア": "{:.3f}".format(avg),
        })

    csv_path = os.path.join(args.outdir, "clips.csv")
    with open(csv_path, "w", newline="", encoding="utf-8-sig") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    print("\n✅ 完了： {} に {} 本 書き出しました（一覧: clips.csv）".format(
        os.path.abspath(args.outdir), len(rows)))


if __name__ == "__main__":
    main()
