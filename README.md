# 塗り絵市場トレンド監視システム (coloring-trend-research)

英語圏(海外版)および日本国内(日本版)の塗り絵市場を調査し、
「今まさに伸び始めていて、まだ競争が激化していないテーマ」を検出して商品化候補を提案するシステムです。
2026-08-31時点では自動実行(週次schedule)を一時停止しており、**チャット経由の手動依頼で運用**しています
(詳細は下記「現在の稼働状況」参照)。

> リポジトリ内には本システムと無関係な `index.html`(衛生管理アプリ)も存在します。
> このREADMEは `research/` `config/` `prompts/` `scripts/` `logs/`
> `.github/workflows/coloring-trend-research.yml` から成るトレンド監視システムについてのみ説明します。

---

## このシステムは何をするのか

毎週、Claude Code(`anthropics/claude-code-action@v1`)が GitHub Actions 上で自律的に:

1. Amazon / Etsy / Pinterest / Google Trends / TikTok・Instagram / Google検索を可能な範囲で調査
2. 新規テーマ候補を最低10個発見
3. 前回(先週)のデータと比較し、上昇・下降・新規・消滅・競合急増を判定
4. 各テーマに Opportunity Score・Momentum Score・Confidence・Trend Stage を付与
5. TOP10、ブルーオーシャン候補(最低5個)、Trend Radarを作成
6. `BUILD_NOW`(今すぐ作る)テーマについて、タイトル案・表紙案・中面アイデア・シリーズ展開まで具体化
7. レポート・履歴・生データを保存し、**リポジトリに自動コミット・プッシュ**

人間が毎週「リサーチして」と指示する必要はありません。

## 毎週いつ実行されるか

**毎週月曜 09:10 JST (= 00:10 UTC)**。00分ちょうどの混雑を避けて意図的に10分ずらしています。

変更する場合は次の2箇所を両方書き換えてください:
- `.github/workflows/coloring-trend-research.yml` の `on.schedule.cron`
- `config/research-config.json` の `schedule.cron_utc` / `schedule.human_readable`

cronはUTC基準です。JSTからUTCへは `JST時刻 - 9時間` で変換してください。

> GitHubの仕様として、スケジュール実行は常にデフォルトブランチから行われ、
> **公開リポジトリの場合はリポジトリに60日間動きがないとスケジュールが自動的に無効化されます**
> (このシステム自身の週次コミットがあれば「動きがある」扱いになるため、通常は問題になりません)。

## 完全自動かどうか

**Secretsの設定が完了していれば完全自動です。** ただし以下は人間側の一度きりの設定が必要です
(下記「必要なSecrets」参照)。設定が完了するまでは、Claudeがワークフローを起動しても
認証エラーで失敗します。

## 手動実行方法

1. GitHubリポジトリの **Actions** タブを開く
2. 左側のワークフロー一覧から **Coloring Book Trend Research (Weekly)** を選択
3. **Run workflow** ボタンを押す(任意で "note" 欄に補足メモを入力可能)

スケジュールを待たずにいつでも実行できます。

## スケジュール変更方法

上記「毎週いつ実行されるか」を参照。cron式は
[crontab.guru](https://crontab.guru/) 等で確認すると安全です(UTC基準で入力すること)。

## 必要なSecrets

このリポジトリの **Settings → Secrets and variables → Actions** で、以下のいずれかを設定してください
(コード中に実際の値を書き込むことは絶対にしないでください)。

| Secret名 | 用途 | 取得方法 |
|---|---|---|
| `ANTHROPIC_API_KEY` | Claude APIキーによる認証(推奨・組織利用向け) | [Claude Console](https://platform.claude.com) でAPIキーを発行 |
| `CLAUDE_CODE_OAUTH_TOKEN` | Claudeサブスクリプション(Pro/Max/Team/Enterprise)による認証 | ローカルで `claude setup-token` を実行して長期トークンを発行 |

どちらか一方で構いません。`CLAUDE_CODE_OAUTH_TOKEN` を使う場合は、
`.github/workflows/coloring-trend-research.yml` 内の `anthropic_api_key:` の行を
`claude_code_oauth_token: ${{ secrets.CLAUDE_CODE_OAUTH_TOKEN }}` に書き換えてください。

さらに、**Claude GitHub Appのインストール**が必要です:
1. https://github.com/apps/claude を開き、このリポジトリにインストールする
2. 権限として Contents / Issues / Pull requests の読み書きを許可する

`GITHUB_TOKEN` はGitHub Actionsが自動発行するため、追加設定は不要です。

## レポートを見る場所

- 週次レポート: `research/reports/YYYY-MM-DD-weekly-report.md`(過去分は削除・上書きされません)
- 最新スナップショット(構造化データ): `research/themes/themes.json`
- 全期間の履歴: `research/history/trend-history.csv` / `research/history/trend-history.json`
- 各市場の生データ: `research/raw/{amazon,etsy,pinterest,google-trends,social,google}/`

> **2026-08-26の初回レポートについて**: `research/reports/2026-08-26-trend-report.md` は
> この自動化システムを構築する前に手動セッションで作成した1回限りのレポートです
> (ファイル名が `-trend-report.md` で、以降の自動生成分の命名規則 `-weekly-report.md` とは異なります)。
> `research/themes/themes.json` と `research/history/trend-history.{csv,json}` は
> このレポート内容を新スキーマ(schema_version 2.0)に移行した上でベースラインとして採用しています。
> 自動化システムによる最初の本番実行が、真の意味での「第1回自動レポート」になります。

## エラー確認方法

1. GitHubの **Actions** タブ → 該当の実行(run)を開く
2. `Run Claude Code weekly research` ステップのログで、Claude自身が何を行い何が失敗したかを確認できる
3. `Validate this week's output` ステップが失敗している場合、
   必須ファイル(レポート/themes.json/history/ログ)のどれかが揃っていないことを意味する
   (このステップはClaudeのステップとは独立して実行されるため、Claudeが「完了しました」と
   自己申告していても実際に成果物が欠けていれば赤くなる)
4. `logs/run-log.md` に各回の実行サマリ(成功ソース/失敗ソース/検出テーマ数など)が追記される
5. 各レポートの `DATA QUALITY REPORT` セクションにも、その回の成功・失敗ソースが記録される

## 費用について

各回の実行で2種類のコストが発生します。

- **GitHub Actions の実行時間**: `ubuntu-latest` ランナーを使用。ジョブには
  `timeout-minutes: 45` の上限を設定済み。
- **Claude APIのトークン使用量**: `claude_args` に `--max-turns 60` を設定し、
  暴走を防止済み。実際の消費量はリサーチの複雑さに依存する。

コストを抑えたい場合は `.github/workflows/coloring-trend-research.yml` の
`--max-turns` を下げる、または `--model` を軽量なモデルに変更する。

**同時多重実行の防止**: `concurrency.group: coloring-trend-weekly-research` を設定しているため、
スケジュール実行と手動実行が重なった場合、後発は先発の完了を待ちます(強制キャンセルはしません)。

## 自動コミットについて

Claudeは調査・分析後、変更したファイル(`research/` `logs/`)を
**このリポジトリの現在のデフォルトブランチに直接コミット・プッシュ**します
(プルリクエストは作成しません)。コミットメッセージの形式:

```
research: weekly coloring trend report YYYY-MM-DD
```

過去のレポート・履歴ファイルの削除・上書きは指示書(`prompts/weekly-research.md`)で
明示的に禁止しています。直接コミットの運用が合わない場合は、
`prompts/weekly-research.md` セクション14の `git push` 部分を
「新しいブランチにpushしてPRを作成する」という指示に書き換えることで、
レビュー付きのフローに変更できます。

## システムの手動テストについて

初回セットアップ後は、本番スケジュールを待たずに一度 **workflow_dispatch で手動実行**し、
以下を確認してください:

- Claudeが起動し、`prompts/weekly-research.md` を読み込んで実行を開始したか
- 各市場のリサーチが(取得不能なものも含めて)記録されたか
- `research/themes/themes.json` が更新されたか
- `research/history/trend-history.csv` / `.json` に新しい日付の行が追加されたか
- `research/reports/YYYY-MM-DD-weekly-report.md` が生成されたか
- `Validate this week's output` ステップが成功(緑)になったか
- `logs/run-log.md` に記録が追記されたか
- コミットが実際にpushされたか

問題が出た場合は `.github/workflows/coloring-trend-research.yml` の実行ログと
`prompts/weekly-research.md` の記述を照らし合わせ、指示の曖昧さやツール権限
(`--allowedTools`)の不足がないか確認してください。

## 現在の稼働状況(2026-08-31時点)

- **海外版塗り絵モジュールの自動実行(schedule)は一時停止中**です。2週連続で「成功」を報告しながら
  実際には調査・保存を一切行わない不具合が発生し、原因調査にも追加費用がかかったため、
  ユーザーの判断で `.github/workflows/coloring-trend-research.yml` の `schedule` トリガーを
  コメントアウトしました。`workflow_dispatch`(手動実行ボタン)はGitHub上に残っていますが、
  原因が解明・修正されるまでは積極的な利用を推奨しません。詳細経緯は `logs/run-log.md` 参照。
- **当面はチャット経由の手動セッションで運用**します(ユーザーが都度「リサーチお願いします」等と
  依頼し、Claude Codeがその場で調査〜レポート作成〜コミットまで行う)。
- **ステッカーモジュールは一時停止中**です(コスト管理のためのユーザー判断。データ・設定は削除していません)。
- 代わりに**日本市場向けの塗り絵モジュール**(`prompts/japan-coloring-research.md`)を追加しました。
  対象はAmazon.co.jp / 楽天市場 / BOOTH・Minne・Creema / X(Twitter)・Instagram日本語圏 /
  Google検索(日本語)。海外版とはデータを完全に分離(`research/themes/themes-japan.json`、
  レポートは `research/reports/YYYY-MM-DD-japan-coloring-weekly-report.md`)して管理します。

## ステッカーモジュールについて(2026-08-27追加、2026-08-31時点で一時停止中)

2026-08-27に、塗り絵モジュールと並ぶ第2の商品カテゴリとして**ステッカーモジュール**を追加しました。
既存の塗り絵モジュール(設定・データ・自動実行)は一切変更していません。

**現状の位置づけ:**
- 調査ロジック: `prompts/sticker-research.md`(塗り絵の`prompts/weekly-research.md`と同じ構成)
- 設定: `config/research-config.json` に追記(`sticker_opportunity_score_weights`, `product_fit`,
  `coloring_fit_criteria` / `sticker_fit_criteria`, `ip_risk_levels`, `trademark_note` 等)
- データ: `research/themes/stickers.json`(塗り絵の`themes.json`とは別ファイル)、
  `research/history/trend-history.csv`/`.json` に `category` 列(`coloring`/`sticker`)を追加して共通管理
- レポート: `research/reports/YYYY-MM-DD-sticker-weekly-report.md`
- **GitHub Actionsへは未接続**(`.github/workflows/coloring-trend-research.yml` は塗り絵モジュールのみを実行する)。手動実行専用
- **Obsidian連携は未着手**。Vaultの場所・OS・Git管理状況等はユーザーのローカルPC環境でないと調査できないため、次回PC作業時の対応事項として残しています

**次回PC作業時に決めていただきたいこと:**
1. Obsidian Vaultをどこに置いているか(パス)、Gitで管理しているか
2. ステッカーモジュールを自動実行する場合、塗り絵と同じワークフローに統合するか、別ワークフローにするか
3. `themes.json`(塗り絵)と`stickers.json`(ステッカー)を将来的に1つの共通Trend Databaseへ統合するかどうか

いずれも、指示書(元の統合指示書)には「既存資産を把握するまで大規模変更を始めない」「勝手に推測パスへ書き込まない」という原則があるため、今回は意図的に着手していません。

## ディレクトリ構成

```
CLAUDE.md
README.md
config/research-config.json
prompts/weekly-research.md              (海外版)
prompts/japan-coloring-research.md      (日本版、2026-08-31追加)
prompts/sticker-research.md             (ステッカー、一時停止中)
scripts/{prepare-research,compare-history,validate-output}.mjs
.github/workflows/coloring-trend-research.yml  (schedule一時停止中、workflow_dispatchのみ)
research/
  raw/{amazon,etsy,pinterest,google-trends,social,google}/         (海外版)
  raw/japan-{amazon,rakuten,handmade,social,google}/                (日本版)
  themes/themes.json          (海外版)
  themes/themes-japan.json    (日本版)
  themes/stickers.json        (ステッカー、一時停止中)
  reports/YYYY-MM-DD-weekly-report.md                     (海外版)
  reports/YYYY-MM-DD-japan-coloring-weekly-report.md      (日本版)
  history/trend-history.{csv,json}   (全モジュール共通、category列で区別)
logs/run-log.md                      (全モジュール共通)
```
