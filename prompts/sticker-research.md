# ステッカー市場 週次トレンド監視ジョブ 実行指示書

このファイルは `prompts/weekly-research.md`(塗り絵モジュール)の姉妹版で、ステッカーモジュールの
調査ロジックをまとめたものです。**現時点ではまだ `.github/workflows/` に接続されておらず、
手動実行専用です**(GitHub Actionsへの組み込み方はREADME.mdの「今後の統合について」を参照)。

すべての判断基準・しきい値・IPブロックリストは `config/research-config.json` に定義されています。
このファイルの指示と `config/research-config.json` は必ず両方読み込んで従ってください。
`prompts/weekly-research.md`(塗り絵)の内容・データを壊さないこと。

---

## 0. あなたの役割

「今すでに売れているステッカー」を見つけるのではなく、**「これから伸びそうなテーマ・世界観・
フレーズを早期発見し、競合が増え切る前に商品化候補を提示する」**こと。

単に「このテーマが流行っている」で終わらせず、最終的に
**「このトレンドは塗り絵にすべきか、ステッカーにすべきか、両方か、まだ待つべきか」**まで判断する
(Product Fit判定、セクション7参照)。

---

## 1. 最初にやること

1. `config/research-config.json` を読む(特に `sticker_opportunity_score_weights`,
   `product_fit`, `sticker_fit_criteria`, `ip_risk_levels`, `trademark_note`)。
2. `node scripts/prepare-research.mjs` をBashで実行し、ディレクトリ・前回スナップショットの有無を確認する。
3. `research/history/trend-history.csv` を読み、`category` 列が `sticker` の行を確認する
   (これが前回のステッカー調査結果。`coloring` 行は塗り絵モジュールのものなので触らない)。
4. 今日の日付を `date -u +%F` で取得する。

---

## 2. データ捏造の絶対禁止

`prompts/weekly-research.md` セクション2と同じルール。BSR・レビュー数・売上・検索数・
Pinterest保存数・TikTok再生数・Etsy販売数などを推測で作成することを禁止する。
取得できない場合は `N/A` とし、理由を記録する。

---

## 3. 調査対象市場

`config/research-config.json` の `markets` を参照。塗り絵モジュールと**同じraw/フォルダを共有**するが、
ファイル名で区別する: `research/raw/<market>/<date>-<market>-sticker-research.md`
(例: `research/raw/etsy/2026-08-27-etsy-sticker-research.md`)。既存の塗り絵側のファイルは
絶対に上書きしない。

- **Etsy(最重要)**: sticker pack, planner stickers, vinyl sticker, digital sticker,
  printable sticker。テーマ・新商品・セット構成・価格・職業/趣味コミュニティ系ニッチを見る。
- **Amazon**: laptop stickers, water bottle stickers, sticker pack 等。
- **Pinterest**: 世界観の先行指標(aesthetic, cozy, kawaii, cottagecore, retro, bookish,
  seasonal, food, animal, hobby, lifestyle, fashion, interior)。
- **TikTok / Instagram**: 文化・ミーム・モチーフ・言葉の先行指標。SNS単体で商品化判断しない。
- **Google Trends**: 候補キーワードの傾き(絶対値でなく上昇/横ばい/下降)。

各市場が取得不能でも、他の市場調査を続行しジョブを止めないこと(取得不能フォーマットは
weekly-research.mdセクション2と同じ)。

---

## 4. 「言葉」の調査(ステッカー特有・重要)

画像モチーフだけでなく、短いフレーズ・スラング・趣味用語・職業ネタ・性格表現・感情表現・
コミュニティ内ジョークも調査対象とする。

**ただし「売れている言葉」＝「自由に使える言葉」ではない。** 既存の番組・歌詞・ブランド・
インフルエンサー発言等の引用が疑われるフレーズは、商品化候補にする場合、
`config/research-config.json` の `trademark_check_required_label`(`"TRADEMARK CHECK REQUIRED"`)
を明示的に付与すること。取得可能な公的商標データベース等で実際に確認できた場合のみ「確認済み」と
書き、確認できないものを安全と断定しない。

---

## 5. テーマ粒度

`主題 × 世界観 × 感情 × 行動 × ターゲット` まで分解する。必要な要素だけ組み合わせる。

悪い例: 猫、犬、花、カエル
良い例: Cozy Cats Baking, Bookish Cats, Sarcastic Office Cats, Cottagecore Frogs,
Retro Food Characters, Sleepy Ghosts, Cute Introvert Animals

---

## 6. スコアリング

### Sticker Opportunity Score(0-100)
`config/research-config.json` の `sticker_opportunity_score_weights` を参照
(需要20/成長性20/競合余地15/一目で伝わる強さ15/セット展開性10/使用場面の広さ10/AI適性10)。

### Momentum Score / Confidence / Trend Stage
`prompts/weekly-research.md` セクション5・9と同じ定義・スケールを使う(塗り絵と共通のものさし)。

### IP Risk
`config/research-config.json` の `ip_risk_levels`(LOW/MEDIUM/HIGH)で評価。
HIGHは原則商品化候補から除外。フレーズ系は上記セクション4の
`TRADEMARK CHECK REQUIRED` ルールに従う。

### Product Fit 判定(ステッカー・塗り絵 横断)
各テーマについて `coloring_fit`(0-100、既存の塗り絵評価基準で採点)と
`sticker_fit`(0-100、`sticker_fit_criteria` で採点)を両方出し、
`config/research-config.json` の `product_fit.categories`
(`COLORING_FIRST` / `STICKER_FIRST` / `BOTH` / `WATCH` / `AVOID`) のいずれかに分類する。

例(指示書より):
```
Trend: Cozy Frog Bakery
Momentum: 86 / Confidence: HIGH / IP Risk: LOW
Coloring Fit: 91 / Sticker Fit: 95
Decision: BOTH
Priority: Sticker first, Coloring second
```

### BUILD NOW / TEST / WATCH / AVOID
`prompts/weekly-research.md` と同じ4分類・同じ目安条件を使う(機械的な足切りにしない)。

**大量生産前にテストする**: ステッカーはまず3〜10商品程度でテストする方針を商品案に明記すること
(いきなり大量のデザインを本制作すべきとは提案しない)。

---

## 7. ステッカー商品企画

BUILD_NOW / TEST判定のテーマについて、
`config/research-config.json` の `sticker_product_ideation_required_fields` の全項目を作成する:

theme, target_customer, sticker_pack_name, 商品タイトル案×10, デザイン案×10〜30,
セット化案, カラーバリエーション, Etsyキーワード候補, Pinterestキーワード候補,
商品説明で訴求する欲求, 使用場面(laptop/planner/journal/water bottle/phone/scrapbook等),
差別化ポイント, IP注意事項(TRADEMARK CHECK REQUIREDの有無を含む)。

---

## 8. レポート構成

保存先: `research/reports/<date>-sticker-weekly-report.md`(既存日付は上書きしない)。

1. **EXECUTIVE SUMMARY**: 今週最重要トレンド／Sticker First TOP3／Coloring First TOP3／
   BOTH TOP3／最大急上昇／最大下落／BUILD NOW／TEST／IP Risk Alert／Saturation Alert
2. **Sticker Opportunities TOP10**(Rank/Theme/Momentum/Confidence/Trend Stage/
   Coloring Fit/Sticker Fit/IP Risk/Decision/Priority)
3. **WHAT CHANGED THIS WEEK**(前回のsticker行と比較。初回は `BASELINE CREATED`)
4. **ブルーオーシャン候補**(最低5個。テーマ｜兆候｜Etsy/Amazon競合｜他市場需要｜総合判断)
5. **THIS WEEK'S BUILD LIST**(Priority順、Theme/Product/Sticker or Coloring or Both/Why/
   Recommended test quantity/IP Risk)
6. **DO NOT BUILD**(理由: 競合過多／Trend下降／IP Risk／データ不足／商品化適性低／一過性バズ)
7. **ステッカー商品企画**(セクション7の内容、BUILD_NOW/TEST全件)
8. **DATA QUALITY REPORT**(成功ソース／失敗ソース／欠損／分析への影響)
9. 該当する場合のみ **RESEARCH INCOMPLETE**

---

## 9. データ保存

1. 生データ: `research/raw/<market>/<date>-<market>-sticker-research.md`
2. `research/themes/stickers.json` を**最新スナップショットで上書き**(themes.jsonと同じ考え方だが
   ステッカー専用。将来的に塗り絵と統合したTrend Databaseに移行する可能性があるが、
   現時点では既存の`themes.json`(塗り絵)を壊さないため別ファイルとする)。
   スキーマは `research/themes/themes.json` を参考にしつつ、`coloring_fit` / `sticker_fit` /
   `product_decision` / `ip_risk_level` を追加すること。
3. `research/history/trend-history.csv` と `.json` に、**`category: "sticker"` の行として追記**
   (塗り絵の行は消さない。列構成は既存と同じ + `category`列)。
4. `logs/run-log.md` に実行記録を追記(`prompts/weekly-research.md` セクション13の4と同じ形式、
   カテゴリをsticker明記)。
5. `node scripts/validate-output.mjs --date <today>` は現状 **塗り絵の `-weekly-report.md` 命名を
   前提**にしているため、ステッカー単独実行時はそのままでは合格しない可能性がある。
   スクリプトを壊さず使う場合は、検証結果を人間が読める形でレポートに書き添えるか、
   将来的に `--category` オプションを追加することを検討する(このセッションでは実装しない)。

---

## 10. 完了の定義

- [ ] 可能な範囲で全市場を調査した(失敗した市場も記録した)
- [ ] フレーズ・スラング調査を行い、商標懸念があるものにTRADEMARK CHECK REQUIREDを付けた
- [ ] Sticker Opportunity / Momentum / Confidence / Trend Stage / IP Risk を全テーマに付与した
- [ ] Coloring Fit / Sticker Fit / Product Fit 判定を行った
- [ ] Sticker Opportunities TOP10を作成した
- [ ] ブルーオーシャン候補を最低5個作成した
- [ ] THIS WEEK'S BUILD LIST と DO NOT BUILD を作成した
- [ ] BUILD_NOW/TESTテーマのステッカー商品企画を作成した
- [ ] research/themes/stickers.json を更新した
- [ ] research/history/trend-history.csv / .json に category=sticker の行を追記した(既存のcoloring行は保持)
- [ ] logs/run-log.md に記録した
- [ ] 塗り絵モジュールのファイル(themes.json, research/reports/の既存ファイル等)を一切変更していないことを確認した
