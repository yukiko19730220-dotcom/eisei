# ステッカー市場トレンドレポート — 2026-08-27

対象市場: 英語圏(米国優先)／Etsy Printables & Stickers中心、Amazon・Pinterest・TikTok/Instagram・Google Trendsで裏付け

このレポートは `prompts/sticker-research.md` に基づく**ステッカーモジュールの初回(ベースライン)調査**です。
`prompts/weekly-research.md`(塗り絵モジュール)のデータ・レポートは一切変更していません。

> **2026-08-27 同日追記**: ユーザーからの追加指示により、TOP3(Book Club & Poetcore / Coquette Bow /
> Goblincore Mushroom & Frog)を28のサブニッチに分解して深掘り検証しました。その結果、
> **Coquette Bow は BUILD_NOW → TEST へ格下げ**、**Goblincore/Frog & Mushroom は Confidence Medium → High へ強化**、
> **Book Club と Poetcore を別テーマとして分離**するなど、いくつかの判定を修正しています。
> 詳細は「サブニッチ深掘り分析」セクションを参照してください。EXECUTIVE SUMMARY・TOP10・BUILD LISTは
> この深掘り結果を反映して更新済みです。

---

## 0. 調査手法と信頼性についての重要な注意

- 本環境のネットワークegressポリシーにより、etsy.com、amazon.com、pinterest.com、trends.google.com、
  tiktok.com、および大半のサードパーティ分析ブログ(accio.com, insightagent.app, asinsight.com等)への
  **直接アクセス(WebFetch)はブロックされました**。
- そのため大半の情報は**WebSearch経由の検索結果スニペット・AI要約**、および実在するEtsy/Amazon商品ページの
  検索結果内タイトル・URLに基づいています。
- **具体的な販売数・レビュー数・Google Trendsの数値グラフは、ほぼ確認できませんでした。** 確認できた
  数少ない一次情報(**Pinterest公式トレンドレポートの成長率データ**)は出典URLを明記し、それ以外の
  「〜と言われている」情報とは明確に区別しています。
- 特にGoogle Trends関連は、accio.com等のAI生成SEOコンテンツファームが「Google Trendsによると」という
  体裁で具体的数値を提示するケースが多数見つかりましたが、**一次ソースを確認できないため、これらの数値は
  一切採用していません**(詳細は `research/raw/google-trends/2026-08-27-google-trends-sticker-research.md` 参照)。
- 数字を推測・捏造した箇所はありません。詳細な生データは `research/raw/{etsy,amazon,pinterest,google-trends,social}/2026-08-27-*-sticker-research.md` を参照してください。

---

## EXECUTIVE SUMMARY(2026-08-27 深掘り後・最新版)

- **今週最重要トレンド**: Frog & Mushroom(Cottagecore/Goblincore)Stickers — 28サブニッチ深掘りの結果、塗り絵・ステッカー双方で実在商品による裏付けが最も強く、Confidence=Highに強化された唯一のテーマ
- **Sticker First TOP3**: ① Book Club Stickers(事実: +243%)　② Frog & Mushroom(全般)Stickers　③ Reading Journal Stickers
- **Coloring First TOP3**: 該当なし(Capybara Sticker Packs が coloring_fit(79) > sticker_fit(70) でColoring Firstに最も近い)
- **BOTH TOP3**: ① Frog & Mushroom / Mushroom Frog / Cottagecore Frog(Goblincoreサブニッチ群)　② Dark Academia Sticker Packs　③ Capybara Sticker Packs
- **BUILD NOW**: Book Club Stickers、Frog & Mushroom(全般)、Mushroom Frog、Cottagecore Frog(4件、うち3件はGoblincoreサブニッチ)
- **TEST**: Coquette Bow(格下げ)、Ballet Bow(新規分離)、Poetcore Stationery(新規分離)、Dark Academia、Gimme Gummy、Curated Clutter/Vintage Travel、Neurodivergent Community Humor、Profession Dark-Humor、Capybara、Goblincore(単語)、Cozy Mushroom
- **IP Risk Alert**: 「Skibidi」「Labubu」は既存IPのため除外(HIGH)。新規発見: 「BookTok」自体がByteDance/TikTokの**登録商標**、「Silent Book Club」も登録商標。カエルモチーフ全般でSanrio「ケロッピ」への意匠寄せに注意(丸い目・赤白ストライプ服の組み合わせを避ける)。「Curated Clutter」「canon event」「6-7」「Sincerely An Introvert類似表現」「Tortured Poets類似表現」がTRADEMARK CHECK REQUIRED(MEDIUM)
- **Saturation Alert**: **Coquette Bow(基準ニッチのPastel Bowは専門書籍まで出版される成熟度、新規追加)**、Dark Academia、Profession Dark-Humor
- **今週見送るべきテーマ**: Pastel Bow基準ニッチ・Cherry Bow・Vintage Bow・Romantic Bow・Books & Coffee・Bow & Books(いずれもCoquette/Book Club深掘りでAVOID判定)、Y2K Holographic/Chrome Finish、Forest Creature(単独)

### 優先順位(3大テーマの最終比較)
評価基準(Momentum/Confidence/競合余地/Sticker Fit/Coloring Fit/IP Risk/商品化スピード/シリーズ展開性)で比較した結果:

**1位: Frog & Mushroom(Cottagecore/Goblincore)** — 3市場確認・Confidence High・BOTH展開・既存塗り絵テーマと直結でシリーズ展開性最強
**2位: Book Club Stickers** — 唯一の一次事実データ(+243%)・商品化スピードは最速だがColoring Fitが低くステッカー単体
**3位: Coquette Bow** — 深掘りの結果、基準ニッチは飽和済みと判明しBUILD_NOWから格下げ。Ballet Bow等の細分化のみ限定的価値

---

## Sticker Opportunities TOP10

| Rank | Theme | Score | Confidence | Trend Stage | Coloring Fit | Sticker Fit | IP Risk | Decision | Priority |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Book Club Stickers(旧: Book Club & Poetcore) | 88 | Medium | 3 | 35 | 90 | LOW(商標確認要) | BUILD_NOW | Sticker First |
| 2 | Coquette Bow Sticker Packs | 85 | Medium | 4 | 45 | 78 | LOW | **TEST**(格下げ) | Sticker First |
| 3 | Dark Academia Sticker Packs | 79 | Medium | 3 | 68 | 82 | LOW | TEST | Both(要監視) |
| 4 | Frog & Mushroom(Cottagecore/Goblincore)Stickers(旧: Goblincore Mushroom & Frog) | 82 | **High**(強化) | 3 | 82 | 90 | LOW(Keroppi意匠注意) | BUILD_NOW | Sticker First, Coloring Second |
| 5 | Gimme Gummy(Candy-Glossy)Stickers | 74 | Low | 1 | 30 | 80 | LOW | TEST | Sticker First |
| 6 | Curated Clutter/Vintage Travel Sticker Collections | 72 | Low | 1 | 40 | 78 | MEDIUM | TEST | Sticker First(商標確認必須) |
| 7 | Neurodivergent/Chronic-Illness Community Humor | 70 | Low | 2 | 20 | 75 | LOW | TEST | Sticker First |
| 8 | Profession Dark-Humor(Nurse/Therapist/Teacher) | 68 | Medium | 4 | 15 | 72 | LOW | TEST | Sticker First |
| 9 | Capybara Sticker Packs | 65 | Low | 3 | 79 | 70 | LOW | TEST | Coloring First, Sticker Second |
| 10 | Y2K Holographic/Chrome Finish Packs | 60 | Low | 2 | 10 | 65 | LOW | WATCH | 監視継続 |
| 11(新規) | Poetcore Stationery Stickers | 62 | Low | 1 | 55 | 75 | MEDIUM(商標確認要) | TEST | Sticker First |
| 12(新規) | Balletcore Bow Sticker Packs | 63 | Low | 2 | 30 | 75 | LOW | TEST | Sticker First |

各テーマの詳細な市場状況・スコア内訳・出典は `research/themes/stickers.json` を参照。11位・12位は今回の深掘りで新たに独立テーマとして分離したもの。

### 各テーマの補足

**1位: Book Club & Poetcore Stationery Stickers**
Pinterest Summer Trend Report 2025で「book club stickers」検索**+243%**、「book club crafts」**+558%**という公式実測値。Pinterest Predicts 2026の「Poetcore」(万年筆・押し花・文学的タイポグラフィ、「the poet aesthetic」+175%)とも世界観が重なる。Etsy/Amazonでの専用商品はまだ手薄で、ステッカーという単語を含む数値が公式一次データで確認できた今回最強のシグナル。ただしPinterest単独市場のため、次回調査でEtsy/Amazonへの波及有無を最優先確認すること。

**2位: Coquette Bow Sticker Packs**
Etsy・Amazon双方で複数の独立出品(56/100/110/500枚パック、ホログラフィック仕上げ含む)を確認。複数の分析ソースが「2026年初頭時点で最もモメンタムが強い」と一致(ただし出典が同一系列サイトに集中しており独立検証は不足)。特定アーティストの画風模倣は避け、オリジナルのリボン・レース・パステル表現に限定する。

**3位: Dark Academia Sticker Packs**
coloring module側でも同テーマ(`dark-academia-gothic-library`, Opportunity Score 68, WATCH判定・saturation_alert)を既に検出済み。ステッカー側もAmazon/Etsyに既に複数出品があり、両カテゴリで競合増加の兆候が一致して見られる、珍しいクロスカテゴリ確認例。大量投入は避け、小ロット検証を推奨。

**4位: Goblincore Mushroom & Frog Stickers**
Etsyで250点/14ページ規模の大型デジタルバンドルを確認。PinterestのWilderkind(繊細な動物モチーフ)トレンドとも重なる。coloring module側の`cottagecore-mushroom-garden`(Opportunity Score 77, TEST)と同一世界観で、既に塗り絵商品も存在するため、**ステッカー先行→塗り絵展開のBOTH戦略**が有効と判断。

**5位: Gimme Gummy(Candy-Glossy)Stickers**
Pinterest Predicts 2026公式トレンド。化粧品ブランドNYXとのコラボ実施報道があり、商業的な検証シグナルとして評価できる。丸み・光沢のあるグミ調質感はステッカーの立体シール表現と相性が良い。ただしEtsy/Amazonでの直接的な裏付けは今回未確認のためConfidence: Low。

**6位: Curated Clutter/Vintage Travel Sticker Collections**
Pinterest 2026 Hobbies Trend Reportの「Curated Clutter」トレンド内で、ヴィンテージコレクション美学の一部として「トラベルステッカー」が公式に名指しされている(ステッカーという単語が明記された数少ない公式例)。**実在の都市名・観光地ロゴ・航空会社等のブランド意匠を模倣しないよう注意**し、パスポートスタンプ風・レトロポストカード風のオリジナル意匠に限定すること(TRADEMARK CHECK REQUIRED)。

**7位: Neurodivergent/Chronic-Illness Community Humor Stickers**
当事者クリエイター発の「ADHD Kitty Sticker Set」等を確認。共感ユーモア軸のコミュニティ発信型ニッチ。当事者の実体験に基づく表現を尊重し、揶揄的にならないよう配慮すること。可能であれば当事者クリエイターとの協業・監修を検討。

**8位: Profession Dark-Humor Stickers(Nurse/Therapist/Teacher)**
看護師系ニッチが特に活発(ブラックユーモア表現)。★5・レビュー335件のショップ(CraftyPugCo)等、既に確立されたセラー多数で競合が厚い(saturation_alert)。新規参入する場合は既存の人気フレーズの丸写しを避け、独自の言い回しで差別化する必要がある。

**9位: Capybara Sticker Packs**
TikTokでDIYカピバラステッカー動画がCraftTok文脈でバイラル化。coloring module側の`capybara-cottagecore`(Opportunity Score 79, TEST, 4位)と同一モチーフで、塗り絵側での検証が先行しているため、塗り絵の反応を見てからステッカーを投入する順番を推奨。

**10位: Y2K Holographic/Chrome Finish Packs**
単一出典(業界メディア)のみで独立裏付けが弱い。ホログラフィック/クロムは「世界観」というより「印刷仕上げ」であり、AI生成イラストだけでは表現しきれない(実際の箔押し・ラミネート加工が必要)ためAI適性が低い(ai_fit: 4/10)。単独商品化より、他テーマ(Coquette等)へのオプション仕上げとして組み込む方が現実的。

---

## サブニッチ深掘り分析(2026-08-27 同日追加、ユーザー指示による)

TOP3テーマ(Book Club & Poetcore / Coquette Bow / Goblincore Mushroom & Frog)について、
28のサブニッチに分解して個別検証しました。詳細な生データは
`research/raw/deep-dive/2026-08-27-*-subniche.md` を、構造化データは
`research/themes/stickers.json` の各テーマの `sub_niches` 配列を参照してください。

### ① Book Club & Poetcore → 「Book Club」と「Poetcore」を分離

**重要: 事実と仮説の区別**
- 【事実】"book club stickers"検索 **+243%**、"book club crafts" +558%、"book club invitations" +173%、"book club hosting" +87%(いずれもPinterest Summer Trend Report 2025公式実測値)
- 【事実、ただし別トレンド】"the poet aesthetic"検索 +175%、"poet core"検索 +75%(Pinterest Predicts 2026、**ファッション/アパレル文脈の数値であり、Poetcore自体が+243%だったわけではない**)
- 【仮説】上記2つの世界観が隣接するため、Poetcoreのステッカー需要も伸びる可能性がある(未検証)

10サブニッチの判定: **BUILD_NOW**=Book Club(中核サブニッチ)／**TEST**=Poetcore・Reading Journal・Dark Academia／**WATCH**=Bookish・Poetry・Library・Literary Girl・Book Club Night／**AVOID**=Books & Coffee(既に飽和)。

**新規IPリスク発見**: 「BookTok」はByteDance/TikTokの**登録商標**(米国登録番号7989376)。「Silent Book Club」もUSPTO登録商標。商品名・タグとしてそのまま使用しないこと。「Hot Girls Read」という類似フレーズが商標出願→コミュニティの反発で撤回された事例もあり、ブッキッシュ・スラングの独占的商標化は評判リスクも伴う。

→ Book Clubは `sticker-book-club-poetcore`(theme_id維持、名称のみ更新)としてBUILD_NOW継続。Poetcoreは仮説段階のため新規theme_id `sticker-poetcore-stationery` として分離しTEST判定。

### ② Coquette Bow → 基準ニッチの飽和が判明、BUILD_NOW→TESTへ格下げ

Amazon上に**『Coquette Stickers: 500+ Frilly, Flirty, and Feminine Stickers』(Adams Media刊)という専門書籍**が既に出版されているレベルで基準ニッチ(Pastel Bow)が成熟していることが判明。「需要はあるが競合が強い場合はBUILD_NOWにしない」というユーザー指示に基づき、`sticker-coquette-bow` 全体の判定を **BUILD_NOW → TEST** に修正し、`saturation_alert: true` を追加しました。

10サブニッチの判定: **TEST**=Bookish Coquette・Dark Coquette・Cherry Bow(弱)・Ballet Bow(最有力)／**WATCH**=Bridal Bow(商品形態が異なる)・French Coquette(判断材料不足)／**AVOID**=Vintage Bow・Pastel Bow(基準、飽和)・Romantic Bow・Bow & Books(Bookish Coquetteに統合)。

最も差別化しやすいのは**Ballet Bow**(balletcoreというファッション上流トレンドは伸びているが、ステッカー特化での供給がまだ薄い)。ただしConfidence Low〜Mediumのため、新規theme_id `sticker-ballet-bow` として小ロットTESTを推奨。

### ③ Goblincore / Mushroom & Frog → Confidence Medium→Highへ強化、塗り絵との内部リンク確立

8サブニッチ調査で、Mushroom Frog・Cottagecore Frog・Frog & Mushroom(全般)の3つがEtsy複数独立セラー・Amazon個別SKU・**既存の塗り絵テーマ`cottagecore-mushroom-garden`**の3方向から裏付けられ、今回の全深掘り調査の中で最も強いエビデンスが得られました。`research/themes/themes.json` の `cottagecore-mushroom-garden` エントリに `related_sticker_theme_id: "sticker-goblincore-mushroom-frog"` を追加し、内部リンクを確立しました。

キーワード需要とビジュアル需要を分離した結果、「Goblincore」という単語自体は2021年バズ(Etsy公式+695%)から鮮度が薄れており2026年Pinterest公式トレンドにも非掲載である一方、**Mushroom/Frog/Cottagecoreというビジュアル・モチーフの需要は単語の人気に関係なく独立して成立**していることが判明。「Frog & Mushroom(全般)」を親カテゴリ、「Mushroom Frog」「Cottagecore Frog」をフレーバーバリエーションとする構成を推奨します。

**重要IP注意(新規発見)**: カエルモチーフ全般でSanrio「ケロッピ(Keroppi)」への意匠寄せ(丸い目・赤白ストライプ服・パステルグリーンの組み合わせ)を避けること。2025〜2026年にSanrioがY2Kノスタルジー路線でケロッピ関連グッズを再展開する動きがあり、既存ip_risk_blocklistの「Sanrio」への間接適用として商品企画時にNGアイデアへ明記します。

商品横展開: Mushroom Frog / Cottagecore Frog / Frog & Mushroom(全般)はいずれも **Both(ステッカー×塗り絵)・Digital Sticker・Printable・Bundle** の全方位に適する、今回調査した3テーマ中もっとも横展開性が高い結果となりました。

---

## WHAT CHANGED THIS WEEK

**BASELINE CREATED**(ステッカーモジュールの初回実行のため、比較対象となる前回データが存在しません)。

`research/history/trend-history.csv` / `.json` に `category: "sticker"` として本日分を記録しました。次回調査時はこのファイルと比較し、順位変動・新規テーマ・消滅テーマを分析します。

なお、以下3テーマは**塗り絵モジュールの既存データとの世界観重複**が確認できました(参考情報):
- Dark Academia(coloring: rank8/68点・WATCH ⇔ sticker: rank3/79点・TEST)
- Cottagecore Mushroom/Goblincore(coloring: rank5/77点・TEST ⇔ sticker: rank4/78点・BUILD_NOW)
- Capybara(coloring: rank4/79点・TEST ⇔ sticker: rank9/65点・TEST)

---

## ブルーオーシャン候補(最低5個)

| テーマ | 兆候 | Etsy/Amazon競合 | 他市場需要 | 総合判断 |
|---|---|---|---|---|
| Book Club & Poetcore Stationery Stickers | Pinterest公式実測値(+243%/+558%/+175%) | 専用パックはまだ手薄 | Pinterest強 | 有望(TOP10 1位にも採用) |
| Gimme Gummy(グミ調グロッシー)ステッカー | Pinterest公式2026トレンド、NYXコラボ | 専用商品ほぼ皆無 | Pinterest単独、成長率数値未確認 | テスト価値あり(TOP10 5位にも採用) |
| Wilderkind(繊細な動物モチーフ)ステッカー | Pinterest記事言及(cute animal aestheticの後継) | 確認できる専用商品なし | 一次未直接確認、確信度Low | コンセプト先行のテスト候補 |
| Neurodivergent/慢性疾患コミュニティ・ユーモアステッカー | Etsyで当事者クリエイター発の商品を確認 | Etsyでも専業ショップは少なく、Amazonでは未確認 | Etsy単独ソース | 早期参入価値あり、当事者視点への配慮が前提(TOP10 7位にも採用) |
| Curated Clutter(ヴィンテージ・トラベルステッカー) | Pinterest公式Hobbiesレポートでステッカーが名指し | 専用カテゴリとしてまだ確立されていない | Pinterest単独 | テスト価値あり、商標確認必須(TOP10 6位にも採用) |

---

## THIS WEEK'S BUILD LIST(2026-08-27 深掘り後・最新版)

**Priority 1**
- Theme: Frog & Mushroom(Cottagecore/Goblincore)— 親カテゴリ
- Product Type: Sticker Pack + 既存塗り絵テーマ`cottagecore-mushroom-garden`との連動キャンペーン(**Both**)
- Priority: 1(今回の深掘りで最も裏付けが強化されたテーマ)
- Why Now: Etsy・Amazon・Pinterest・塗り絵書籍の4方向から裏付け、Confidence=High。既存塗り絵テーマとの内部リンク確立済み
- Recommended Test Quantity: ステッカー12〜15デザイン、塗り絵は既存シリーズへ追加数ページ
- IP Risk: LOW(**Sanrio「ケロッピ」風の意匠は避けること**)
- Etsy Keyword: cottagecore frog mushroom sticker, frog and mushroom sticker pack
- Pinterest Keyword: frogcore aesthetic, cottagecore mushroom
- Cross-sell Opportunity: 塗り絵`cottagecore-mushroom-garden`とのバンドル販売、ステッカー購入者への塗り絵レコメンド

**Priority 2**
- Theme: Book Club Stickers
- Product Type: Sticker Pack("The Poet's Shelf" Sticker Collection)(**Sticker Only**)
- Priority: 2(唯一の一次事実データ、商品化スピード最速)
- Why Now: Pinterest公式実測値"book club stickers"+243%が本調査全体で最も確度の高いシグナル
- Recommended Test Quantity: 15〜20デザイン
- IP Risk: LOW(ただし**「BookTok」「Silent Book Club」は登録商標のため商品名に使わない**)
- Etsy Keyword: book club stickers, reading journal stickers
- Pinterest Keyword: book club aesthetic, bookish stationery
- Cross-sell Opportunity: 現時点で塗り絵側に直接対応するテーマなし(coloring_fit低)。将来「コージー読書」系塗り絵テーマが検出されれば連携候補

**Priority 3**
- Theme: Cottagecore Frog(Goblincoreのフレーバーバリエーション)
- Product Type: Sticker Pack(**Both**、Priority 1の横展開)
- Priority: 3
- Why Now: 単独でもEtsy専用マーケットページ複数、塗り絵側との親和性がPriority1に次いで高い
- Recommended Test Quantity: 8〜10デザイン
- IP Risk: LOW(同上ケロッピ注意)
- Etsy Keyword: cottagecore frog sticker
- Pinterest Keyword: cottagecore frog aesthetic
- Cross-sell Opportunity: Priority1のバンドルに統合可能

**Priority 4**
- Theme: Balletcore Bow Sticker Packs(新規分離)
- Product Type: Sticker Pack(**Sticker Only**、小規模探索的テスト)
- Priority: 4
- Why Now: ファッション/Pinterestの上流トレンドは伸びているが、ステッカー特化での供給がまだ薄い空白地帯候補。ただしConfidence Low〜Mediumのため小ロットに留める
- Recommended Test Quantity: 5〜8デザイン(探索的)
- IP Risk: LOW
- Etsy Keyword: balletcore bow sticker
- Pinterest Keyword: balletcore aesthetic
- Cross-sell Opportunity: なし(現時点で独立商品)

**Priority 5**
- Theme: Poetcore Stationery Stickers(新規分離、仮説検証)
- Product Type: Sticker Pack(**Sticker Only**、小規模探索的テスト)
- Priority: 5
- Why Now: Book Clubに次いで隣接する仮説だが実測値なし。競合が薄いうちに安価に検証する価値あり
- Recommended Test Quantity: 5〜8デザイン(探索的)
- IP Risk: MEDIUM(**「Tortured Poets」に類似した言い回しを避けること**)
- Etsy Keyword: poetcore stickers, fountain pen stickers
- Pinterest Keyword: poet aesthetic, poetcore
- Cross-sell Opportunity: Priority2(Book Club)のデラックス版バンドルに含めることも検討可

**参考(見送りから再検討候補への降格)**: Coquette Bow Sticker Packs全体(旧Priority2)は、深掘りの結果BUILD_NOWからTESTへ格下げしたため、上記Priority 1〜5には含めていません。Bookish Coquette / Dark Coquetteは次回以降の追加テスト候補として`research/themes/stickers.json`のsub_niches内に記録済みです。

---

## DO NOT BUILD

| テーマ/要素 | 理由 |
|---|---|
| Skibidi関連グッズ全般 | HIGH IPリスク。「SKIBIDI TOILET」はInvisible Narratives社が商標登録済みで訴訟も発生中 |
| Labubu風モンスターマスコットの模倣 | HIGH IPリスク。Pop Mart社の明確な既存IP、商標保護・模倣品への法的措置が明言されている |
| 「Canon Event」「6-7」を映画ロゴ/キャラ意匠・楽曲ビジュアルと結びつけた商品 | 商標・著作権懸念(TRADEMARK CHECK REQUIRED)。テキスト単体の一般語的用法にとどめない限りリスクあり |
| Sanrio/Rilakkuma/Monchhichi/Tamagotchi等の既存キャラクター模倣 | config/research-config.jsonのip_risk_blocklistに抵触する既存IP |
| Y2K Holographic/Chrome Finishの単独商品化 | データ不足(単一出典)。「世界観」ではなく「仕上げ材質」トレンドのため、独立商品より既存テーマへのオプションとして扱うべき |
| Low Cortisol関連の既存アニメ/ゲームキャラクター模倣版 | フレーズ自体は低リスクだが、派生画像がThe Amazing Digital Circus・ウマ娘等の既存IPと組み合わさって拡散しているため、そうした絵柄の模倣は既存IP侵害リスク |
| Pastel Bow(基準ニッチ)単独 | 専門書籍まで出版される成熟度(Trend Stage 4〜5相当)。新規単独参入は非推奨 |
| Cherry Bow / Vintage Bow / Romantic Bow / Bow & Books | いずれもコモディティ化済み、または他ニッチ(Pastel Bow/Bookish Coquette)と実質重複 |
| Books & Coffee(Book Clubサブニッチ) | Etsyで3,000件超規模を示唆する飽和カテゴリ、汎用的すぎて差別化困難 |
| 「BookTok」「Silent Book Club」をそのまま冠した商品名 | いずれも登録商標。商品タイトル・タグとしての直接使用は避ける |
| Forest Creature(単独) | 既存出版ブランド(Dylanna Press, Jade Summer等)多数の成熟レッドオーシャン |
| カエルモチーフのSanrio「ケロッピ」風デザイン | 丸い目・赤白ストライプ服・パステルグリーンの組み合わせは既存IPへの意匠寄せとみなされるリスク |

---

## ステッカー商品企画(BUILD_NOWテーマ)

### ① Book Club & Poetcore Stationery Stickers

- **Theme**: Book Club & Poetcore Stationery Stickers
- **Target Customer**: 20〜35歳、読書コミュニティ(BookTok/BookClub)参加者、万年筆・文房具愛好家、ジャーナリング習慣を持つ層
- **Sticker Pack Name**: "The Poet's Shelf" Sticker Collection

**商品タイトル案×10**
1. The Poet's Shelf: Bookish Sticker Collection
2. Book Club Essentials Sticker Pack
3. Fountain Pen & Pressed Flowers Sticker Set
4. Cozy Reading Nook Stickers for Journals
5. Literary Life Sticker Pack: For Book Lovers
6. Poetcore Aesthetic Sticker Sheet
7. My TBR Pile Sticker Collection
8. Bookish Stationery Stickers for Planners
9. Ink & Pages Sticker Pack
10. Book Club Meeting Planner Stickers

**デザイン案×15**
積み上げた本 / 万年筆とインク瓶 / 押し花のしおり / ティーカップと本 / TBR(積読)タワー / 読書灯とブランケット / 手書き風の引用文フレーム / 図書館の本棚 / ブックマーク各種 / 読書ジャーナルのページめくり / 眼鏡と本 / コーヒーの染みと本 / 手紙とペン先 / 詩集の表紙風アイコン / 読書会カレンダーアイコン

**セット化案**: 「エッセンシャル10枚セット」「デラックス30枚セット」「月替わり読書会テーマパック(季節ごとの本の表紙色に合わせる)」

**カラーバリエーション**: セピア/アイボリー(クラシック)、パステルラベンダー(ソフト)、ダークアカデミア寄りの深緑・バーガンディ

**Etsyキーワード候補**: book club stickers, bookish sticker pack, reading journal stickers, poetcore stickers, fountain pen stickers, literary stickers, TBR stickers

**Pinterestキーワード候補**: poetcore aesthetic, book club ideas, bookish stationery, reading journal inspo

**商品説明で訴求する欲求**: 「読書という孤独な趣味を、可視化できる愛着のあるコレクションに変えたい」「自分の読書ジャーナルを特別なものにしたい」

**使用場面**: journal, planner, laptop, bullet journal, gift for book club members

**差別化ポイント**: 既存の「本」ステッカーは単なる本の絵が多いが、本商品は「文通・万年筆・押し花」というPoetcoreの世界観を統合し、読書会という社会的活動そのものを祝う切り口にする

**IP注意事項**: 特定の実在する書籍タイトル・表紙デザイン・出版社ロゴを使用しない。架空の本のタイトル・抽象的な本のシルエットにとどめる

---

### ② Coquette Bow Sticker Packs

- **Theme**: Coquette Bow Sticker Packs
- **Target Customer**: 15〜25歳、TikTok/Pinterestのcoquette美学フォロワー、プランナー・スクラップブック愛好家
- **Sticker Pack Name**: "Ribbons & Lace" Coquette Collection

**商品タイトル案×10**
1. Ribbons & Lace: Coquette Sticker Pack
2. Pastel Bow Sticker Collection
3. Coquette Aesthetic Stickers for Laptop & Journal
4. Sweet Bow Sticker Sheet
5. Dainty Ribbons Sticker Pack
6. Coquette Core Sticker Bundle
7. Ballet Pink Bow Stickers
8. Vintage Coquette Sticker Set
9. Holographic Bow Sticker Pack
10. Soft Girl Coquette Stickers

**デザイン案×15**
大小さまざまなリボン / レースの縁取り / パールのアクセント / ハートとリボンの組み合わせ / バレエシューズ / 手紙とシーリングワックス / 香水瓶 / チェリーモチーフ / ミルクグラス / キャンドル / 花冠 / 蝶々とリボン / パステルの雲 / ロケットペンダント / ミニチュアケーキ

**セット化案**: 「パステル基本セット15枚」「ホログラフィック特別版」「モノクロ(白黒リボンのみ)ミニマル版」

**カラーバリエーション**: ベビーピンク/ラベンダー(定番)、バニラアイボリー(ミニマル)、ホログラフィック(プレミアム)

**Etsyキーワード候補**: coquette stickers, bow sticker pack, aesthetic laptop stickers, coquette aesthetic, ribbon stickers

**Pinterestキーワード候補**: coquette aesthetic, bow aesthetic, soft girl era, coquette room decor

**商品説明で訴求する欲求**: 「かわいさを恥ずかしがらずに全面に出したい」「甘さの中に自分らしい上品さを表現したい」

**使用場面**: laptop, water bottle, planner, journal, gift wrapping decoration

**差別化ポイント**: 既に飽和気味の市場のため、単なるリボンのイラストではなく「香水瓶」「シーリングワックス」等の周辺小物まで含めた世界観の一貫性で差別化する

**IP注意事項**: 特定アーティストの署名的な画風(特定のリボンの結び方・タッチ)の模倣は避ける。既存キャラクター(Sanrio等)とのコラボ的意匠にしない

---

### ③ Goblincore Mushroom & Frog Stickers

- **Theme**: Goblincore Mushroom & Frog Stickers
- **Target Customer**: 18〜35歳、cottagecore/goblincore美学フォロワー、「変な生き物が好き」なZ世代、塗り絵モジュールの`cottagecore-mushroom-garden`購入層とも重複
- **Sticker Pack Name**: "Toadstool & Friends" Goblincore Collection

**商品タイトル案×10**
1. Toadstool & Friends: Goblincore Sticker Pack
2. Frog in the Forest Sticker Collection
3. Mushroom Cottage Sticker Sheet
4. Goblincore Aesthetic Stickers
5. Whimsical Woodland Creatures Sticker Pack
6. Cozy Frog & Mushroom Bundle
7. Dark Cottagecore Nature Stickers
8. Forest Floor Sticker Collection
9. Goblin Garden Sticker Set
10. Mossy Mushroom Friends Stickers

**デザイン案×15**
きのこの家 / カエルの傘さし / きのこ狩りかご / 苔むした石 / カタツムリと葉っぱ / どんぐりの帽子 / 妖精のランタン / カエルの王冠 / 森のきのこ図鑑風 / 蛙の合唱 / 落ち葉とハリネズミ / 木の洞の家 / 水たまりとカエル / きのこの妖精 / 森の入り口の看板

**セット化案**: 「フォレストベーシック10枚」「デラックス30枚(きのこ図鑑風解説カード付き)」— coloring版`cottagecore-mushroom-garden`のカバーデザインとモチーフを揃えたクロスセルバンドルも検討

**カラーバリエーション**: アースカラー(定番)、ダークコテージコア(深緑・バーガンディ)、パステル(ライト版)

**Etsyキーワード候補**: goblincore stickers, mushroom sticker pack, cottagecore frog stickers, forest aesthetic stickers, whimsical nature stickers

**Pinterestキーワード候補**: goblincore aesthetic, cottagecore mushroom, wilderkind, forest witch aesthetic

**商品説明で訴求する欲求**: 「完璧に整った可愛さより、少し変で愛おしい自然の世界に浸りたい」「デジタル疲れから森の静けさへ逃避したい」

**使用場面**: journal, water bottle, laptop, plant pot decoration, gift for nature lovers

**差別化ポイント**: 塗り絵モジュールの`cottagecore-mushroom-garden`と世界観・キャラクターデザインを統一し、「ステッカーで気に入ったら塗り絵も」「塗り絵のファンにステッカーも」という双方向のクロスセルを狙う

**IP注意事項**: 既存の人気きのこキャラクター(トロールやスーパーマリオのキノコ等)を想起させる意匠は避け、実際のきのこ・カエルの生態的特徴に基づいたオリジナルデザインにする

---

## DATA QUALITY REPORT

**成功ソース**: Etsy(WebSearch経由)、Amazon(WebSearch経由)、Pinterest公式トレンドレポート(WebSearch経由の要約、複数の一次データを含む数値を確認)、TikTok/Instagram(ニュース・トレンド分析記事経由)

**失敗ソース**: etsy.com/amazon.com/pinterest.com/trends.google.com/tiktok.comへの直接WebFetch(全面ブロック)。多数のサードパーティ分析ブログ(accio.com, insightagent.app, asinsight.com, everbee.io等)の本文全体(WebSearchスニペットのみ利用)

**欠損データ**: Google Trendsの実測値(全キーワード未確認)。Etsy/Amazonの実売数・レビュー数・BSR相当指標(ほぼ全件N/A)。TikTok/Instagramの実際の再生数・エンゲージメント数値

**分析への影響**: 本レポートのConfidenceは全体的にLow〜Mediumにとどまる(High判定は0件)。特にPinterest単独ソースのテーマ(Book Club & Poetcore、Gimme Gummy)はスコアが高くても市場横断的な裏付けが薄く、次回調査でEtsy/Amazonへの波及を最優先で確認する必要がある。Google Trendsは今回実質的に機能しておらず、AI生成SEOコンテンツファーム由来の数値を誤って採用しないよう特に注意を払った。

---

## 今後のアクション

1. `research/history/trend-history.csv` / `.json` に本日分(category=sticker)を記録済み。次回調査はこれと比較すること
2. Book Club & Poetcore、Gimme Gummy、Curated ClutterはPinterest単独ソースのため、次回調査でEtsy/Amazon側の実商品有無を最優先確認する
3. Dark Academia・Goblincore・Capybaraはcoloring moduleと世界観が重複するため、両カテゴリのスコア推移を並べて追跡する価値がある(将来的な共通Trend Database統合の検討材料)
4. フレーズ系候補(TRADEMARK CHECK REQUIRED)は、取得可能であれば次回以降USPTO等の公的商標データベースでの実際の確認を試みること
5. 【2026-08-27深掘り追加】Ballet Bow・Poetcore Stationeryは仮説段階のため、次回調査でEtsy/Amazonへの実際の波及有無を最優先確認すること
6. Obsidian連携は今回も未着手(ユーザーのPC作業時に対応予定)。research/themes/stickers.json・trend-history.{csv,json}への記録は完了しているため、Obsidian接続時にそのままインポート可能な状態
