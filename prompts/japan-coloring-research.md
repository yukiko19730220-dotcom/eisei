# 塗り絵市場(日本版) 週次トレンド監視ジョブ 実行指示書

このファイルは `prompts/weekly-research.md`(海外版・英語圏)と対をなす、**日本国内市場向け**の
指示書です。目的・判断基準の骨格は海外版と同じですが、対象プラットフォーム・言語・
市場慣習が異なるため独立したファイルにしています。

現時点ではGitHub Actionsには接続されておらず、**人間からの直接依頼(チャット)による手動実行専用**です。

すべての判断基準・しきい値・Trend Stage定義・IPブロックリストの共通部分は
`config/research-config.json` に定義されています。このファイルの指示と
`config/research-config.json`(特に `japan_markets` / `ip_risk_blocklist_jp_additional` セクション)を
必ず両方読み込んで従ってください。

---

## 0. あなたの役割

海外版と同じく、あなたは単発のリサーチャーではありません。「日本国内の塗り絵市場を監視し、
売れ始める前兆を検出し、商品化候補を自動提案する市場監視システム」の日本市場担当です。

**最重要目的**：「今まさに一番売れているテーマ」を見つけることではなく、
**「需要が伸び始めているが、まだ競争が完全に激化していないテーマ」を発見すること**。

---

## 1. 海外版との違い(重要)

1. **対象言語・市場が日本語/日本国内のみ**。英語圏の調査結果(`research/themes/themes.json`)とは
   完全に別データとして扱う。混同・合算しない。
2. **対象プラットフォームが異なる**(`config/research-config.json` の `japan_markets.markets` 参照):
   - Amazon.co.jp
   - 楽天市場
   - BOOTH / Minne / Creema(日本の同人・ハンドメイド系販売サイト。printable/デジタルダウンロードの
     ぬりえ・イラスト素材が多数出品されている。海外版におけるEtsyに近い位置づけ)
   - X(旧Twitter) / Instagram の日本語圏
   - Google検索(日本語、一般トレンド記事・ブログ・ニュース)
3. **日本の塗り絵市場は英語圏と客層・文脈が異なる可能性がある**ことを意識すること。例:
   - シニア層向け「脳トレ」「介護・レクリエーション施設向け」需要が独立して存在する
   - キャラクターもの(アニメ・漫画・VTuber等)への需要が非常に強いが、
     ほとんどが既存IPに紐づくため商品化候補としては使えない(下記4参照)
   - 英語圏で強い"cozy"(コージー)"cottagecore"のような美学が日本語圏でも同じ強さで
     機能するとは限らない。日本語圏独自のトレンド語(例:「ゆるかわ」「エモい」「量産型」等)や
     季節行事(お正月・お花見・七夕等)も観察すること
   - 「大人の塗り絵」というジャンル自体は日本でも既に確立された市場(コロナ禍前後からブーム)
     であるため、英語圏のような「新興ジャンル」という位置づけではなく、
     成熟市場の中でのニッチ発掘という視点になりやすい点に留意する
4. **IPリスクが特に高い**。`config/research-config.json` の共通 `ip_risk_blocklist` に加えて、
   `ip_risk_blocklist_jp_additional` を必ず確認すること。日本市場は既存アニメ・漫画・VTuber・
   同人作家の画風模倣への意識が特に強い分野なので、「〜風」であっても特定作品・特定個人を
   明確に想起させる企画は商品化候補として一切提案しないこと。

---

## 2. データ捏造の絶対禁止

海外版と同じ原則。売上・レビュー数・検索数・SNS言及数などを推測で作成することを禁止する。
取得できない場合は必ず `N/A` とし、理由(取得不能／ログイン必須／CAPTCHA／有料データ／
利用規約上の制約／技術的に取得不可能など)を記録すること。

---

## 3. 調査対象市場(可能な範囲ですべて)

`config/research-config.json` の `japan_markets.markets` を参照。各市場のraw出力は
`research/raw/japan-<market>/<date>-japan-<market>-research.md` という
ファイル名で保存すること(既存日付のファイルは絶対に上書きしない)。

1. **Amazon.co.jp** — 大人の塗り絵、ぬりえ、マンダラ塗り絵、動物の塗り絵、花の塗り絵、
   グレースケール塗り絵などを起点に検索し、関連商品からテーマを横展開する。
   出版日・レビュー数・ランキング等は取得できれば記録し、できなければN/A。
2. **楽天市場** — 塗り絵関連の商品(書籍・グッズ・デジタルダウンロード含む)を検索する。
3. **BOOTH / Minne / Creema** — printable(印刷用データ)のぬりえ・イラスト素材、
   同人イベント発の塗り絵本などを検索する。「Amazonでは弱いがこれらのサイトで
   売れ始めているテーマ」を特に重要視する(海外版のEtsyと同じ位置づけ、先行シグナルの可能性)。
4. **X(Twitter) / Instagram 日本語圏** — 「#塗り絵」「#ぬりえ」等のハッシュタグでの話題化を
   確認する。未来需要の先行指標として使うが、SNSだけ流行 → 即商品化は禁止。
5. **Google検索(日本語)** — 一般的なライフスタイル・トレンド記事、ぬりえ専門ブログ、
   出版社のプレスリリース等を検索する。

各市場について、アクセスできなかった場合は無理に突破せず「取得不能」を記録し、
**他の市場の調査は必ず続行する**こと。1つの市場が失敗してもジョブ全体を止めない。

---

## 4. クロスマーケット分析・テーマ粒度・新規テーマ発見・スコアリング

海外版(`prompts/weekly-research.md` セクション4〜9)と同じ考え方を適用する。
Opportunity Score / Momentum Score / Confidence / Trend Stage の定義、
Velocity Alert 🚨 / Saturation Alert ⚠️、季節性分析も共通の枠組み
(`config/research-config.json` の `opportunity_score_weights` / `trend_stages` /
`confidence_levels` / `alerts` / `seasonal_keywords`)をそのまま使う
(海外版・日本版で重みを分ける必要が生じた場合は、その旨をこのファイルと
`config/research-config.json` に明記した上で `opportunity_score_weights_japan` を新設すること。
現時点ではまだ分けていない)。

**IPリスクは前述のセクション1-4を最優先で確認すること。**

---

## 5. 商品化判断(4分類)

`decision_categories`(`BUILD_NOW` / `TEST` / `WATCH` / `AVOID`)を参照。海外版と同じ英語enumを使う。

---

## 6. BUILD NOWテーマの商品企画

海外版セクション11と同じ項目(タイトル案×10・サブタイトル案×5・表紙案×5・中面アイデア×30・
シリーズ展開案×10・想定ユーザー・購入動機・検索キーワード・差別化ポイント・NG案)を作成する。
ただし言語は**日本語で企画する**(タイトル案も日本語のタイトル案とする。海外版のような
英語タイトルは不要)。検索キーワードもAmazon.co.jp/楽天/BOOTH等での実際の検索語(日本語)を使う。

---

## 7. レポート作成

保存先: `research/reports/<YYYY-MM-DD>-japan-coloring-weekly-report.md`
(UTC日付、既存ファイルは絶対に上書きしない)。

構成は海外版セクション12と同じ順番(EXECUTIVE SUMMARY → TOP10 → WHAT CHANGED THIS WEEK →
ブルーオーシャン候補 → Trend Radar → 商品企画 → DATA QUALITY REPORT → 必要なら
RESEARCH INCOMPLETE)。冒頭に「対象市場: 日本国内(Amazon.co.jp / 楽天市場 / BOOTH・Minne・Creema /
X・Instagram日本語圏)」と明記すること。

---

## 8. データ保存

1. 各市場の生調査結果 → `research/raw/japan-<market>/<date>-japan-<market>-research.md`(出典URL必須)
2. `research/themes/themes-japan.json` を**今週の最新スナップショットで上書き**する
   (海外版の `research/themes/themes.json` とは別ファイル。スキーマは海外版を参考にしつつ、
   `theme_id` の先頭に `jp-` を付けて海外版と衝突しないようにする。例: `jp-neko-mandala`)。
3. `research/history/trend-history.csv` と `.json` に、**今週分の行/レコードを追記**する
   (共有履歴ファイル。`category` 列には `coloring_japan` を使うこと。過去の行は絶対に消さない)。
   **注意**: `scripts/compare-history.mjs` は `category` を区別せず「直近の日付」を選んでしまう
   既知の制限がある(2026-08-31の海外版レポートのDATA QUALITY REPORT参照)。日本版の前回データと
   比較する際は、`trend-history.json` を `category === "coloring_japan"` でフィルタした一時ファイルを
   自分で作成してから `compare-history.mjs --history <一時ファイル>` を実行すること。
4. `logs/run-log.md` に今回の実行記録を追記する(海外版と共有のログファイル。
   見出しに「(日本市場)」等を付けて区別すること)。
5. `node scripts/validate-output.mjs --date <today>` は**海外版の成果物(`research/themes/themes.json`他)
   のみをチェックする設計**であり、日本版の成果物はこのスクリプトの対象外。日本版は
   目視で「レポート・themes-japan.json・history追記・run-log追記」がすべて揃っているか確認すること。

---

## 9. 最後にやること: コミット & プッシュ

海外版セクション14と同じ手順。過去のレポート・履歴ファイルを削除・上書きするコマンドは
絶対に使わないこと。

---

## 10. 完了の定義

海外版セクション15と同じ基準を、日本版の成果物(`themes-japan.json`、
`-japan-coloring-weekly-report.md` 等)に置き換えて適用する。
