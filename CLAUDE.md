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
- **塗り絵モジュール**(`prompts/weekly-research.md`): 2026-08-26開始。GitHub Actionsで毎週自動実行される(接続済み)
- **ステッカーモジュール**(`prompts/sticker-research.md`): 2026-08-27追加。現時点では手動実行専用(GitHub Actions未接続)。Obsidian連携・ローカル実行環境の確認は、ユーザーのPC環境で行う予定のため未着手
- 両モジュールは `config/research-config.json` の一部設定(市場一覧・IPブロックリスト・Trend Stage定義等)を共有しつつ、スコアリング基準(Opportunity Score重み)は別々に持つ。詳細は同ファイルの `categories` / `sticker_opportunity_score_weights` / `product_fit` を参照
- テーマが両モジュールで重複する場合(例: Dark Academia, Cottagecore Mushroom, Capybara)、`coloring_fit` / `sticker_fit` を比較し `COLORING_FIRST` / `STICKER_FIRST` / `BOTH` を判断する(`research/themes/stickers.json` 参照)

## システム構成

```
CLAUDE.md                  ← このファイル
README.md                  ← 運用マニュアル(人間向け)
config/research-config.json ← スコア重み・しきい値・市場一覧・IPブロックリスト等の単一情報源
prompts/weekly-research.md  ← 週次ジョブが実行時に読む詳細指示書(実際の調査ロジックはここに集約)
scripts/
  prepare-research.mjs      ← ディレクトリ準備・現状把握
  compare-history.mjs       ← 前回スナップショットとの差分計算
  validate-output.mjs       ← 今週分の成果物が揃っているかの最終チェック
.github/workflows/coloring-trend-research.yml ← 毎週月曜09:10 JST自動実行 + 手動実行
research/
  raw/{amazon,etsy,pinterest,google-trends,social,google}/ ← 市場別の生調査データ
  themes/themes.json        ← 最新スナップショット(毎週上書き)
  reports/YYYY-MM-DD-weekly-report.md ← 週次レポート(絶対に上書きしない、追加のみ)
  history/trend-history.{csv,json}    ← 全週の履歴(追記専用)
logs/run-log.md             ← 実行ログ(追記専用)
```

## 調査対象市場

Amazon / Etsy / Pinterest / Google Trends / TikTok・Instagram / Google検索の最低6系統。
1つの市場が取得不能でも、他の市場の調査を続行し、ジョブ全体を止めない。

## 絶対厳守のルール

1. **データ捏造は完全禁止。** BSR・レビュー数・売上・検索数・Pinterest保存数・TikTok再生数・
   Etsy販売数などを推測で作成してはならない。取得できない場合は `N/A` とし、理由を記録する。
2. **過去データとの比較は必須。** 毎回、前回のレポート・履歴を読み込み、新規登場・上昇・下降・
   消滅・競合増減・クロスマーケット化を判定する(初回のみ `BASELINE CREATED`)。
3. **複数市場での確認を必須とする。** 1市場だけの情報で「トレンド」と断定しない。SNSのバズだけで
   即商品化を判断しない。
4. **著作権・商標への配慮。** Disney、Pokémon、Sanrio等の既存IP、有名キャラクター、有名作家/ブランドの
   画風模倣は商品化候補として一切推奨しない(ブロックリストは `config/research-config.json` の
   `ip_risk_blocklist` を参照)。ステッカーモジュールでは特に**フレーズ・スラング**も調査対象となるため、
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

`.github/workflows/coloring-trend-research.yml` が毎週月曜09:10 JST(00:10 UTC)に
`anthropics/claude-code-action@v1` を起動し、このClaude自身に `prompts/weekly-research.md` を
読ませて自律実行させる。手動実行は GitHub Actions の workflow_dispatch から可能。
詳細な運用方法は `README.md` を参照。

このプロジェクトで作業する際(手動セッションであっても)は、上記のルールと
`prompts/weekly-research.md` の指示に従うこと。
