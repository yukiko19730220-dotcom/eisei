# CLAUDE.md

このファイルは、Claude Codeがこのリポジトリを開いた際に「何を目的としたプロジェクトなのか」を
毎回理解できるようにするためのものです。

> **スコープの注意**: このリポジトリのルートには、本システムとは無関係な `index.html`
> (衛生管理アプリ／HACCP記録)も存在します。この CLAUDE.md が説明するのは、
> `research/` `config/` `prompts/` `scripts/` `logs/` `.github/workflows/coloring-trend-research.yml`
> から構成される「物販トレンド監視システム(塗り絵モジュール＋ステッカーモジュール)」についてのみです。

## プロジェクト目的

**塗り絵・ステッカー等の物販市場(英語圏、Amazon KDP + Etsy中心)を毎週自動監視し、
「需要が伸び始めているが、まだ競争が激化していないテーマ」を検出し、
商品化候補(どちらの商品形態にすべきかの判断を含む)を自動提案するシステム。**

最重要目的は「今一番売れている商品」を見つけることではない。
売れてから追いかけるのではなく、**売れ始めの兆候(Trend Stage 1〜3、特にStage 2)を捕まえる**こと。

### モジュール構成
- **塗り絵モジュール(海外版)**(`prompts/weekly-research.md`): 2026-08-26開始。対象は英語圏(Amazon KDP + Etsy中心)。GitHub Actionsでの毎週自動実行は2026-08-31時点で**一時停止中**(2週連続で「成功」を報告しながら実際には何も生成しない不具合が発生したため。詳細は `logs/run-log.md` 参照)。当面は手動セッション(チャットでの都度依頼)で運用する
- **塗り絵モジュール(日本版)**(`prompts/japan-coloring-research.md`): 2026-08-31追加。対象は日本国内(Amazon.co.jp / 楽天市場 / BOOTH・Minne・Creema / X・Instagram日本語圏 / 一般のGoogle検索(日本語))。手動実行専用(GitHub Actions未接続)。海外版とはテーマ・データを完全に分離して管理する(`research/themes/themes-japan.json`、レポートは `-japan-coloring-weekly-report.md`)
- **ステッカーモジュール**(`prompts/sticker-research.md`): 2026-08-27追加、**2026-08-31時点で一時停止中**(ユーザーの判断によるコスト管理のため。既存データ・設定は削除していないので、再開時はそのまま利用できる)
- 各モジュールの現在の稼働状況は `config/research-config.json` の `module_status` を参照。塗り絵モジュール(海外版・日本版)とステッカーモジュールは `config/research-config.json` の一部設定(Trend Stage定義・IPブロックリスト共通部分等)を共有しつつ、スコアリング基準(Opportunity Score重み)・市場一覧・保存先ファイルは別々に持つ。詳細は同ファイルの `categories` / `markets` / `japan_markets` / `sticker_opportunity_score_weights` / `product_fit` / `ip_risk_blocklist_jp_additional` を参照
- テーマが複数モジュールで重複する場合(例: Dark Academia, Cottagecore Mushroom, Capybara)、`coloring_fit` / `sticker_fit` を比較し `COLORING_FIRST` / `STICKER_FIRST` / `BOTH` を判断する(`research/themes/stickers.json` 参照。ステッカーモジュールは一時停止中だが判断基準自体は維持する)

## システム構成

```
CLAUDE.md                  ← このファイル
README.md                  ← 運用マニュアル(人間向け)
config/research-config.json ← スコア重み・しきい値・市場一覧・IPブロックリスト等の単一情報源
prompts/weekly-research.md  ← 週次ジョブ(海外版)が読む詳細指示書
prompts/japan-coloring-research.md ← 日本版の詳細指示書(2026-08-31追加)
prompts/sticker-research.md ← ステッカーモジュールの詳細指示書(2026-08-31時点で一時停止中)
scripts/
  prepare-research.mjs      ← ディレクトリ準備・現状把握
  compare-history.mjs       ← 前回スナップショットとの差分計算(category区別に既知の制限あり、DATA QUALITY REPORT参照)
  validate-output.mjs       ← 海外版塗り絵モジュールの成果物が揃っているかの最終チェック(日本版・ステッカー版は対象外)
.github/workflows/coloring-trend-research.yml ← 海外版塗り絵モジュール用。scheduleは2026-08-31時点で一時停止中、workflow_dispatchのみ残存
research/
  raw/{amazon,etsy,pinterest,google-trends,social,google}/ ← 海外版の市場別生データ
  raw/japan-{amazon,rakuten,handmade,social,google}/ ← 日本版の市場別生データ
  themes/themes.json        ← 海外版の最新スナップショット(毎週上書き)
  themes/themes-japan.json  ← 日本版の最新スナップショット(毎週上書き)
  themes/stickers.json      ← ステッカーモジュールの最新スナップショット(一時停止中)
  reports/YYYY-MM-DD-weekly-report.md ← 海外版週次レポート(絶対に上書きしない、追加のみ)
  reports/YYYY-MM-DD-japan-coloring-weekly-report.md ← 日本版週次レポート(同上)
  history/trend-history.{csv,json}    ← 全モジュール共通の全週履歴(追記専用、category列で区別)
logs/run-log.md             ← 全モジュール共通の実行ログ(追記専用)
```

## 調査対象市場

- **海外版**: Amazon / Etsy / Pinterest / Google Trends / TikTok・Instagram / Google検索の最低6系統。
- **日本版**: Amazon.co.jp / 楽天市場 / BOOTH・Minne・Creema / X(Twitter)・Instagram日本語圏 /
  Google検索(日本語)の最低5系統。詳細は `prompts/japan-coloring-research.md` を参照。

いずれも1つの市場が取得不能でも、他の市場の調査を続行し、ジョブ全体を止めない。

## 絶対厳守のルール

1. **データ捏造は完全禁止。** BSR・レビュー数・売上・検索数・Pinterest保存数・TikTok再生数・
   Etsy販売数などを推測で作成してはならない。取得できない場合は `N/A` とし、理由を記録する。
2. **過去データとの比較は必須。** 毎回、前回のレポート・履歴を読み込み、新規登場・上昇・下降・
   消滅・競合増減・クロスマーケット化を判定する(初回のみ `BASELINE CREATED`)。
3. **複数市場での確認を必須とする。** 1市場だけの情報で「トレンド」と断定しない。SNSのバズだけで
   即商品化を判断しない。
4. **著作権・商標への配慮。** Disney、Pokémon、Sanrio等の既存IP、有名キャラクター、有名作家/ブランドの
   画風模倣は商品化候補として一切推奨しない(ブロックリストは `config/research-config.json` の
   `ip_risk_blocklist` を参照)。**日本版塗り絵モジュールは、これに加えて `ip_risk_blocklist_jp_additional`
   (ちいかわ・すみっコぐらし・ドラえもん等の日本国内で特に意識すべきIP、およびVTuber・同人作家個人の
   画風模倣)も必ず確認すること。** ステッカーモジュールでは特に**フレーズ・スラング**も調査対象となるため、
   「売れている言葉」＝「自由に使える言葉」ではない点に注意し、既存作品・楽曲・ブランド由来の疑いがある
   フレーズには `TRADEMARK CHECK REQUIRED` を明示する(`config/research-config.json` の
   `trademark_note` / `ip_risk_levels` 参照)。
5. **最終判断基準。** 各テーマは Opportunity Score(0-100)・Momentum Score(0-100、初回はN/A)・
   Confidence(High/Medium/Low)・Trend Stage(0-6)を付けたうえで、
   `BUILD_NOW` / `TEST` / `WATCH` / `AVOID` のいずれかに分類する。しきい値は目安であり、
   機械的な足切りにせず、例外がある場合は理由を明記する。
6. **保存場所を厳守する。** raw / themes / reports / history / logs は明確に分離し、
   `research/reports/` と `research/history/` と `logs/` は追記専用(過去分を削除・上書きしない)。
7. **レポート形式。** `prompts/weekly-research.md` のセクション12に定義された構成
   (EXECUTIVE SUMMARY → TOP10 → WHAT CHANGED THIS WEEK → ブルーオーシャン候補 → Trend Radar →
   商品企画 → DATA QUALITY REPORT → 必要ならRESEARCH INCOMPLETE)に厳密に従う。

## 週次自動実行について

`.github/workflows/coloring-trend-research.yml` は本来、毎週月曜09:10 JST(00:10 UTC)に
`anthropics/claude-code-action@v1` を起動し、`prompts/weekly-research.md`(海外版塗り絵モジュール)を
読ませて自律実行させる設計だが、**2026-08-31時点でscheduleトリガーは一時停止中**(詳細は
`logs/run-log.md` 参照)。workflow_dispatchボタンは残っているが積極利用は非推奨。
日本版・ステッカーモジュールはそもそもGitHub Actions未接続で、常に手動実行のみ。
詳細な運用方法は `README.md` を参照。

このプロジェクトで作業する際(手動セッションであっても)は、上記のルールと、
対象モジュールに応じて `prompts/weekly-research.md`(海外版)・`prompts/japan-coloring-research.md`
(日本版)・`prompts/sticker-research.md`(ステッカー、一時停止中)のいずれかの指示に従うこと。
