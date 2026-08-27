# ステッカー市場トレンドレポート — 2026-08-27

対象市場: 英語圏(米国優先)／Etsy Printables & Stickers中心、Amazon・Pinterest・TikTok/Instagram・Google Trendsで裏付け

このレポートは `prompts/sticker-research.md` に基づく**ステッカーモジュールの初回(ベースライン)調査**です。
`prompts/weekly-research.md`(塗り絵モジュール)のデータ・レポートは一切変更していません。

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

## EXECUTIVE SUMMARY

- **今週最重要トレンド**: Book Club & Poetcore Stationery Stickers — Pinterest公式実測値(book club stickers検索+243%)という、今回の調査全体で最も確度の高い一次データに基づく
- **Sticker First TOP3**: ① Book Club & Poetcore Stationery Stickers　② Coquette Bow Sticker Packs　③ Gimme Gummy(Candy-Glossy)Stickers
- **Coloring First TOP3**: 該当なし(ステッカー適性が塗り絵適性を上回るテーマが大半。強いて挙げれば Capybara Sticker Packs は coloring_fit(79) が sticker_fit(70) をわずかに上回るためColoring Firstに近い)
- **BOTH TOP3**: ① Dark Academia Sticker Packs　② Goblincore Mushroom & Frog Stickers　③ Capybara Sticker Packs — いずれも既存の塗り絵モジュールで検出済みのテーマと世界観が重なる
- **BUILD NOW**: Book Club & Poetcore Stationery Stickers、Coquette Bow Sticker Packs、Goblincore Mushroom & Frog Stickers(3件)
- **TEST**: Dark Academia、Gimme Gummy、Curated Clutter/Vintage Travel、Neurodivergent Community Humor、Profession Dark-Humor、Capybara(6件)
- **IP Risk Alert**: 「Skibidi」「Labubu」関連は既存IPのため商品化候補から除外(HIGH)。「Curated Clutter/Vintage Travel」は実在地名・ブランド意匠を避ける必要がありTRADEMARK CHECK REQUIRED(MEDIUM)。フレーズでは「canon event」「6-7」「Sincerely An Introvert類似表現」がTRADEMARK CHECK REQUIRED
- **Saturation Alert**: Dark Academia(塗り絵・ステッカー両方で競合急増の兆候)、Profession Dark-Humor(看護師系ニッチは既に確立済みセラーが多数)
- **今週見送るべきテーマ**: Y2K Holographic/Chrome Finish(単一出典・独立裏付け弱く、そもそも「世界観」ではなく「仕上げ材質」のトレンドのためWATCH)

---

## Sticker Opportunities TOP10

| Rank | Theme | Score | Confidence | Trend Stage | Coloring Fit | Sticker Fit | IP Risk | Decision | Priority |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Book Club & Poetcore Stationery Stickers | 88 | Medium | 1 | 45 | 92 | LOW | BUILD_NOW | Sticker First |
| 2 | Coquette Bow Sticker Packs | 85 | Medium | 3 | 55 | 90 | LOW | BUILD_NOW | Sticker First |
| 3 | Dark Academia Sticker Packs | 79 | Medium | 3 | 68 | 82 | LOW | TEST | Both(要監視) |
| 4 | Goblincore Mushroom & Frog Stickers | 78 | Medium | 2 | 77 | 85 | LOW | BUILD_NOW | Sticker First, Coloring Second |
| 5 | Gimme Gummy(Candy-Glossy)Stickers | 74 | Low | 1 | 30 | 80 | LOW | TEST | Sticker First |
| 6 | Curated Clutter/Vintage Travel Sticker Collections | 72 | Low | 1 | 40 | 78 | MEDIUM | TEST | Sticker First(商標確認必須) |
| 7 | Neurodivergent/Chronic-Illness Community Humor | 70 | Low | 2 | 20 | 75 | LOW | TEST | Sticker First |
| 8 | Profession Dark-Humor(Nurse/Therapist/Teacher) | 68 | Medium | 4 | 15 | 72 | LOW | TEST | Sticker First |
| 9 | Capybara Sticker Packs | 65 | Low | 3 | 79 | 70 | LOW | TEST | Coloring First, Sticker Second |
| 10 | Y2K Holographic/Chrome Finish Packs | 60 | Low | 2 | 10 | 65 | LOW | WATCH | 監視継続 |

各テーマの詳細な市場状況・スコア内訳・出典は `research/themes/stickers.json` を参照。

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

## THIS WEEK'S BUILD LIST

**Priority 1**
- Theme: Book Club & Poetcore Stationery Stickers
- Product: Sticker Pack("Bookish Poet" Sticker Collection)
- Sticker / Coloring / Both: **Sticker**
- Why: 今回の調査で唯一、Pinterest公式一次データが直接「ステッカー」という単語で+243%を記録。文房具・読書コミュニティという裾野の広いターゲット
- Recommended test quantity: 15〜20デザイン
- IP Risk: LOW

**Priority 2**
- Theme: Coquette Bow Sticker Packs
- Product: Sticker Pack("Coquette Bow Collection")
- Sticker / Coloring / Both: **Sticker**
- Why: Etsy・Amazon双方で既にモメンタムが確認できる、最も裾野の広いティーン〜20代女性向けテーマ
- Recommended test quantity: 15デザイン(カラーバリエーション違いも1デザインとしてカウント)
- IP Risk: LOW(特定作家画風の模倣を避けること)

**Priority 3**
- Theme: Goblincore Mushroom & Frog Stickers
- Product: Sticker Pack + 既存塗り絵テーマ(`cottagecore-mushroom-garden`)との連動キャンペーン
- Sticker / Coloring / Both: **Both**
- Why: Etsyで実証済みの需要(250点規模バンドル)＋塗り絵側で既に検証中のテーマとの相乗効果
- Recommended test quantity: ステッカー10デザイン、塗り絵は既存シリーズの追加ページとして数枚
- IP Risk: LOW

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
