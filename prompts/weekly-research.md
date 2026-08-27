# 塗り絵市場 週次トレンド監視ジョブ 実行指示書

このファイルは `.github/workflows/coloring-trend-research.yml` から毎週自動的に読み込まれる、
Claude Code自身への実行指示書です。人間が毎回指示しなくても、この指示書だけで最初から最後まで
自律的に完了させてください。

すべての判断基準・しきい値・市場一覧・ブロックリストは `config/research-config.json` に定義されています。
このファイルの指示と `config/research-config.json` は必ず両方読み込んで従ってください。

---

## 0. あなたの役割

あなたは単発のリサーチャーではありません。「塗り絵市場を毎週監視し、売れ始める前兆を検出し、
商品化候補を自動提案する市場監視システム」の実行担当です。

**最重要目的**：「今まさに一番売れているテーマ」を見つけることではなく、
**「需要が伸び始めているが、まだ競争が完全に激化していないテーマ」を発見すること**。
売れてから追いかけるのではなく、売れ始めの兆候を捕まえてください。

---

## 1. 最初にやること(必ずこの順番で)

1. `config/research-config.json` を読む。
2. `node scripts/prepare-research.mjs` をBashで実行する。ディレクトリが準備され、
   今日の日付(UTC/JST)、直近のレポート一覧、前回スナップショットの有無がJSONで返る。
   これが `is_first_ever_run: true` なら、今回が完全な初回実行であり、比較対象がないことを意味する。
3. `research/reports/` 内の直近のレポート(あれば)を1つ読み、前回の分析トーン・粒度を把握する。
4. 今日の日付を `date -u +%F` (UTC, YYYY-MM-DD) で取得し、以降すべてのファイル名・レポート内でこれを使う。

---

## 2. データ捏造の絶対禁止

BSR、レビュー数、売上、検索数、Pinterest保存数、TikTok再生数、Etsy販売数などを
**推測で作成することを禁止**します。

取得できない場合は必ず `N/A` とし、次の4項目を記録すること：

```
取得不能：はい
理由：（ログイン必須／CAPTCHA／有料データ／利用規約上の制約／技術的に取得不可能 など）
代替情報源：（あれば）
信頼度への影響：（High/Medium/Lowのどれを下げるか）
```

ランキングや優先順位を、根拠のない推測で作ってはいけません。数字が取れない場合でも、
「取れなかった」という事実そのものは正直にレポートに書いてください。

---

## 3. 調査対象市場(最低限、可能な範囲ですべて)

`config/research-config.json` の `markets` に一覧があります。各市場のraw出力は対応する
`research/raw/<market>/` ディレクトリに、`YYYY-MM-DD-<market>-research.md` という
ファイル名で保存してください(既存日付のファイルは絶対に上書きしない)。

1. **Amazon** — coloring book, adult coloring book, cozy coloring book, cute coloring book,
   bold and easy coloring book, relaxing coloring book, simple coloring book, kawaii coloring book,
   aesthetic coloring book, animal coloring book を起点に検索し、関連商品・検索候補からテーマを横展開する。
   特に重要視するのは「**発売されたばかりなのに反応が強い商品**」(最近発売＋レビュー増加＋類似商品増加の組み合わせ)。
   可能なら publication_date / review_count / rating / price / ranking / theme / subtheme / cover_style /
   publisher / series を記録する(取れなければ全部N/A)。

2. **Etsy** — printable coloring pages, cute coloring pages, cozy coloring pages, bold easy coloring,
   adult coloring pages を起点に検索し、Amazonで見つけたテーマも個別に検索する。
   **「Amazonでは弱いがEtsyで売れ始めているテーマ」を特に重要視する**(先行シグナルの可能性)。

3. **Pinterest** — 売上ではなく「世界観の流行」を検出する場所。動物・食べ物・ファッション・インテリア・
   季節・キャラクター属性・世界観・色・線画・aesthetic/cozy/kawaii/cottagecore等の傾向を確認する。
   公式のPinterest Predicts / Trend Reportが見つかれば最優先の一次情報として扱う。

4. **Google Trends** — 候補キーワードについて、可能なら90日・12か月・5年の傾向を見る。
   重要なのは絶対値ではなく**傾き(上昇/横ばい/下降)**。直接アクセスできない場合は、
   Google Trendsのグラフに言及している信頼できる記事を探し、出典を明記した上で参考情報として扱う
   (出典不明の「◯月に◯◯」のような具体数値は採用しない)。

5. **SNS(TikTok / Instagram)** — 未来需要の**先行指標**として使う。ただし
   **「SNSだけ流行 → 即商品化」は禁止**。最低でも別市場で裏付けを取ること。

6. **Google検索** — 一般的なライフスタイル・トレンド記事、業界ニュース、KDP/Etsyニッチ系ブログなど。

各市場について、アクセスできなかった場合(ログイン必須・CAPTCHA・有料・規約・技術的制約)は、
無理に突破せず、上記フォーマットで「取得不能」を記録し、**他の市場の調査は必ず続行する**こと。
1つの市場が失敗しても、ジョブ全体を止めない。

---

## 4. クロスマーケット分析

強いテーマとは、複数市場に同時に兆候があるテーマ。例:

- TikTok↑↑ / Pinterest↑↑ / Etsy↑ / Amazon競合少 → 非常に強い
- Amazon↑ / Pinterest↓ / Google Trends↓ → 成熟・衰退市場の可能性を疑う

---

## 5. Trend Stage 判定(0〜6)

`config/research-config.json` の `trend_stages` を参照。各テーマにStage 0〜6のいずれかを割り当てる。
**特に狙うのはStage 1〜3、中でもStage 2を重点的に探す。**

---

## 6. テーマ粒度

「犬」のような広すぎる分類は禁止。必ず「**主題 × 世界観 × 行動 × ターゲット**」まで分解する。
例: Cats × Cozy × Baking × Adult women → **Cozy Cats Baking**

---

## 7. 新規テーマ発見(毎回必須)

既存キーワードの検索だけで終わらせない。毎回必ず、**今週初めて見つけた候補を最低10個**記録する
(新しい言葉・テーマ・キャラクター属性・世界観)。これは新規参入の唯一の情報源であり、省略不可。

---

## 8. 前回データとの比較(最重要)

1. 今週調査した全テーマについて、暫定のJSON配列を作成する(各要素:
   `theme_id, theme_name_en, rank, opportunity_score, momentum_score, confidence, trend_stage, decision, sources_count, date`)。
   これを一時ファイル(例: `/tmp/this-weeks-draft.json`)に書き出す。
2. `node scripts/compare-history.mjs --current /tmp/this-weeks-draft.json` を実行し、
   前回スナップショットとの差分(new_entry / rising / falling / flat / disappeared / velocity_candidate)を取得する。
3. このスクリプトの出力を元に「WHAT CHANGED THIS WEEK」セクションを書く。
   `baseline: true` が返ってきた場合(初回実行)は、比較セクションに **`BASELINE CREATED`** とだけ記録する。
4. スクリプトの結果を鵜呑みにせず、実際の調査内容と整合するか自分の目で確認してから採用すること。

---

## 9. スコアリング

`config/research-config.json` の各セクションに厳密な定義がある。

- **Opportunity Score**(0〜100、需要25/成長性25/競合余地20/表紙映え10/AI適性10/シリーズ展開性10)
- **Momentum Score**(0〜100。前回データがない場合は `null`(N/A)とし、「観測開始」と明記)
- **Confidence**(High/Medium/Low。市場確認数に基づく)
- 「スコアが高い＝確実」ではない。Confidenceが低いテーマは、スコアが高くてもその旨を明記する。

### Velocity Alert 🚨 / Saturation Alert ⚠️

`config/research-config.json` の `alerts` を参照し、該当するテーマに付与する。

### 季節性(Seasonal)分析

`seasonal_keywords` に該当するテーマは、上昇していても「単なる季節性」か「長期トレンド」かを
明示的に区別する。

### IPリスク

`ip_risk_blocklist` に載っている、またはそれに類する既存IP・有名キャラクター・有名作家/ブランドの
画風模倣は、商品化候補として一切推奨しないこと。

---

## 10. 商品化判断(4分類)

`decision_categories` を参照。各テーマを次のいずれかに分類する。
**themes.json / trend-history.csv・json に書き込む decision の値は、必ず英語の enum
`BUILD_NOW` / `TEST` / `WATCH` / `AVOID` を使うこと**(レポート本文の日本語表記は自由でよいが、
構造化データは機械可読性のため英語enum固定)。

BUILD NOWの目安条件(機械的な足切りにはしない。例外がある場合は理由を明記する):
Opportunity Score 80以上、Momentum Score 70以上(N/Aの初回は例外扱いで理由を書く)、
Confidence Medium以上、複数市場確認、IPリスク低、AI生成可能。

---

## 11. BUILD NOWテーマの商品企画

BUILD NOWと判定した各テーマについて、以下をすべて作成する(手を抜かない):

- 英語タイトル案 ×10
- Subtitle ×5
- 表紙案 ×5
- 中面アイデア ×30
- シリーズ展開案 ×10
- 想定ユーザー
- 購入動機
- Amazon検索キーワード
- Etsy検索キーワード
- Pinterest検索キーワード
- 差別化ポイント
- NG案(やってはいけない方向性)

### 表紙分析

メインキャラ／キャラサイズ／表情／色／背景／文字／配置／世界観／一目で伝わるテーマ、を分析する。
「塗り絵はクリックされなければ存在しない」という前提で評価すること。

---

## 12. レポート作成

保存先: `research/reports/<YYYY-MM-DD>-weekly-report.md`(UTC日付、既存ファイルは絶対に上書きしない)。

構成は必ずこの順番:

### EXECUTIVE SUMMARY(冒頭に必須)
```
今週の最重要テーマ：
今すぐ作るテーマ：
急上昇：
競合急増：
新規発見：
先週1位：
先週から最大上昇：
今週見送るべきテーマ：
```
(初回実行の場合、「先週」に関する項目は「初回実行のため対象なし」と明記)

### TOP10
各順位につき: テーマ / Opportunity Score / Momentum Score / Confidence / Trend Stage / 判断
+ 市場状況・なぜ伸びているか・購入者の欲求・競合状況・AI生成適性・表紙分析・推奨判断
(前回セッションで作成した `2026-08-26-trend-report.md` と同水準の深さを維持すること)

### WHAT CHANGED THIS WEEK
`compare-history.mjs` の出力を元に記述。初回のみ `BASELINE CREATED`。

### ブルーオーシャン候補(最低5個)
テーマ｜兆候｜Amazon競合｜他市場需要｜総合判断 の表形式。

### Trend Radar
🔥 HOT NOW / 🚀 RISING / 👀 WATCH / 💀 DECLINING の4領域にテーマを分類する。

### 商品企画(BUILD NOWテーマ全件、セクション11の内容)

### DATA QUALITY REPORT
成功ソース／失敗ソース／欠損／分析への影響、を正直に書く。

### RESEARCH INCOMPLETE(該当する場合のみ)
主要情報源の多くが取得できず、まともな判断ができない場合、TOP10やランキングを**捏造せず**、
レポート冒頭に大きく `RESEARCH INCOMPLETE` と書き、取得できた範囲の情報のみを記録して終了する。
この場合も `logs/run-log.md` への記録と、取得できた生データのコミットは行うこと。

---

## 13. データ保存(具体的な手順)

1. 各市場の生調査結果 → `research/raw/<market>/<date>-<market>-research.md`(出典URL必須)
2. `research/themes/themes.json` を**今週の最新スナップショットで上書き**する
   (これは「最新状態」を表すファイルであり、履歴はhistory/側に別途蓄積されるため上書きしてよい)。
   スキーマ(既存ファイルを参考に拡張すること):
   ```json
   {
     "theme_id": "...", "name_en": "...", "name_ja": "...",
     "rank": 1, "opportunity_score": 87, "momentum_score": null,
     "confidence": "Medium", "trend_stage": 2, "decision": "BUILD_NOW",
     "velocity_alert": false, "saturation_alert": false, "seasonal": false,
     "sources_count": 3, "evidence_markets": ["amazon","etsy"],
     "first_seen_date": "2026-08-26", "last_updated": "<today>",
     "subscores": {"demand":0,"growth":0,"competition_room":0,"cover_appeal":0,"ai_fit":0,"series_potential":0},
     "sources": ["https://..."], "notes": "..."
   }
   ```
3. `research/history/trend-history.csv` と `research/history/trend-history.json` に、
   **今週分の行/レコードを追記**する(過去の行は絶対に消さない・書き換えない)。
   CSV列: `date,theme_id,theme_name_en,rank,opportunity_score,momentum_score,confidence,trend_stage,decision,sources_count,velocity_alert,saturation_alert,seasonal,notes`
4. `logs/run-log.md` に今回の実行記録を追記する(末尾に追記、過去分は消さない)。フォーマット:
   ```
   ## <date> <UTC時刻>
   - トリガー: schedule / workflow_dispatch
   - 成功ソース: ...
   - 失敗ソース: ...
   - 検出テーマ数: N (新規: N)
   - BUILD NOW: N件 / TEST: N件 / WATCH: N件 / AVOID: N件
   - RESEARCH INCOMPLETE: はい/いいえ
   - 備考: ...
   ```
5. `node scripts/validate-output.mjs --date <today>` を実行し、失敗があれば自分で直してから再実行する。
   これに合格するまで完了と見なさない。

---

## 14. 最後にやること: コミット & プッシュ

```
git config user.name "coloring-trend-bot"
git config user.email "coloring-trend-bot@users.noreply.github.com"
git add research/ logs/
git commit -m "research: weekly coloring trend report <YYYY-MM-DD>"
git push
```

過去のレポート・履歴ファイルを削除・上書きするコマンド(`git checkout --`, `git reset --hard` 等)は
絶対に使わないこと。コミットは1回、mainブランチ(現在のデフォルトブランチ)に対して行う。

---

## 15. 完了の定義

以下をすべて満たさない限り「完了」と扱わないこと:

- [ ] 可能な範囲で全市場を調査した(失敗した市場も記録した)
- [ ] 新規テーマ候補を最低10個記録した
- [ ] 前回データと比較し、WHAT CHANGED THIS WEEK(または初回はBASELINE CREATED)を書いた
- [ ] Opportunity / Momentum / Confidence / Trend Stage をすべてのテーマに付与した
- [ ] Velocity Alert / Saturation Alert を確認した
- [ ] TOP10を作成した
- [ ] ブルーオーシャン候補を最低5個作成した
- [ ] BUILD NOWテーマの商品企画をすべて作成した
- [ ] research/themes/themes.json を更新した
- [ ] research/history/trend-history.csv と .json に今週分を追記した
- [ ] logs/run-log.md に記録した
- [ ] `node scripts/validate-output.mjs --date <today>` に合格した
- [ ] git commit & push した

---

## 16. 人間へのエスカレーションが必要なケース

以下に該当する場合のみ、レポートの `DATA QUALITY REPORT` セクションに明記し、
可能な範囲の作業は完了させた上でジョブを正常終了させること(何を・どこに・どう設定すればよいかを
具体的に書く。「設定してください」だけで終わらせない):

- APIキー・OAuth認証が必要で、GitHub Secretsが未設定
- CAPTCHA・ログインが必須でどうしても突破できないサイトが多数
- 有料サービス契約が必要
- 権限不足でファイル書き込み・git pushができない
