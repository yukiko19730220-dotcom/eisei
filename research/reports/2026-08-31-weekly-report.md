# 塗り絵市場トレンドレポート — 2026-08-31

対象市場: 英語圏（米国優先、英国・カナダ・オーストラリア）／Amazon KDP塗り絵本・Etsy Printable Coloring Pages

---

## 0. 調査手法と信頼性についての重要な注意（今回の特記事項）

**先週(2026-08-31予定分)の自動実行(GitHub Actions)は、実際には調査を何も行わずに「成功」を報告して終了するという不具合が発生し、成果物が一切生成されていませんでした。** 本レポートは、その欠落を埋めるためにチャット経由で手動再構築したものです。調査手法・品質基準自体は自動実行時と同一の指示書(`prompts/weekly-research.md`)に従っています。

- 本セッションでも先週(2026-08-26/27)と同様、`amazon.com`・`etsy.com`・`pinterest.com`・`trends.google.com`・`tiktok.com`への**直接WebFetchアクセスはネットワークegressプロキシにより`EGRESS_BLOCKED`でブロック**されました。一般のニュース・ブログサイトの多くも今回は同様にWebFetchがブロックされ(`kdpeasy.com`, `coloringbook.dev`, `coloringqueen.net`, `newsroom.pinterest.com`等)、**大半の情報はWebSearchツールが返す検索結果スニペット・AI要約に基づいています**。
- **具体的な販売数・レビュー数・Google Trendsの数値グラフは、今回もほぼ確認できませんでした。** 確認できた数少ない一次情報(Pinterest公式2026 Hobbies Trend Report / Predicts 2026の成長率数値)は出典URLを明記し、それ以外の「〜と言われている」情報とは明確に区別しています。数字を推測・捏造した箇所はありません。
- 詳細な生データ・出典一覧は `research/raw/{amazon,etsy,pinterest,google-trends,social,google}/2026-08-31-*.md` を参照してください。
- **前回データとの比較について重要な注意**: `research/history/trend-history.json`には塗り絵モジュール(coloring)とステッカーモジュール(sticker)のスナップショットが日付混在で格納されています。`node scripts/compare-history.mjs`をそのまま実行すると「直近の日付」として2026-08-27(ステッカーモジュールのスナップショット)が誤って選択され、塗り絵の全テーマが「新規」、ステッカーの全テーマが「消滅」と誤判定される問題を確認しました。本レポートでは`trend-history.json`をcategory="coloring"でフィルタした一時ファイルを作成し、正しい前回スナップショット(2026-08-26)と比較し直しています。この既知の問題は本レポート末尾のDATA QUALITY REPORTにも記録し、`scripts/compare-history.mjs`自体をcategoryでフィルタできるよう改修することを次回への申し送り事項とします。

---

## EXECUTIVE SUMMARY

- **今週の最重要テーマ**：Cozy Cafe & Bookstore Series(今週1位、複数市場で安定成長)と、Analog Lifestyle / Digital-Detox Ritual Coloring(先週のブルーオーシャン監視項目から一気にBUILD_NOW入り)
- **今すぐ作るテーマ**：Cozy Cafe & Bookstore Series／Cozy Kitchen Witch／Analog Lifestyle & Digital-Detox Ritual Coloring
- **急上昇**：Analog Lifestyle / Digital-Detox Ritual Coloring🚨(確認市場数が実質1→4に拡大)、Goblincore Coloring🚨(新規テーマがいきなり4市場で確認)
- **競合急増**：Cozy Kitchen Witch⚠️(先週数点→Amazonで7〜8点)、Dark Academia Gothic Library⚠️(Amazonで9点以上に増加継続)、Cottagecore Mushroom & Garden⚠️(Amazonで9点以上、Etsyでも高密度)
- **新規発見**：Goblincore／Old Money・Quiet Luxury Lifestyle／Cryptid・Cryptozoology／Urban Jungle・Cozy Plant Lady／Liminal Space・Backrooms・Weirdcore／Coquette／Farmcore・Cozy Farm Animals／Cosmic Reset(占星術・タロット・クリスタル)／Wilderkind／Backyard Botanist／Axolotl単体ニッチ／Moo Deng／Fairycore／Weekend Equestrian／Handmade Hacker／Curated Clutter(要IP注意)の計15件以上(最低10件を達成)
- **先週1位**：Cozy Kitchen Witch(87点)
- **先週から最大上昇**：ランキング変動ではCozy Cafe & Bookstore Series(3位→1位)。「圏外→BUILD_NOW」という質的ジャンプではAnalog Lifestyle / Digital-Detox Ritual Coloringが最大。
- **今週見送るべきテーマ**：Grandmacore Cottage Coloring(BUILD_NOW→TESTへ格下げ、1週間経っても実商品化が進まず)、Dark Academia Gothic Library(競合急増が加速、参入タイミングとして遅い可能性)、Capybara Cozy & Cottagecore(供給は増加継続だが需要指標は頭打ちの兆候)

---

## TOP10

### 1位：Cozy Cafe & Bookstore Series（コージー・カフェ＆ブックストア）

総合点：**86/100**(先週84)　Momentum：**55/100**　Confidence：**High**　Trend Stage：**3**　判断：**今すぐ作る(BUILD_NOW)**

**市場状況**
- Amazon：「Cozy Cafe Coloring Book」「Cozy Bookstore Coloring Book」「Cozy Café」「My Cozy Bookstore Coffee」「Cozy Bookshops and Cafes Coloring Book」「Cute & Cozy Bookstore」「The Bookstore Café」など**7点以上**を確認。新たに「Cozy Library Coloring Book」(猫+読書コーナー+コテージコア書店)という隣接派生を発見。
- Etsy：新規出品を追加確認（Coffee Shop Moments Bundle、Cozy Coffee Shop Coloring Book、Cozy Bookshop Coloring Page＝cottagecore bookstoreとも明示的にタグ付け）。出品ペースは継続。
- Pinterest：直接データはないが、Fall 2026 Hobbies Trend Reportの新トレンド「Home Café Engineering」(banana syrup recipe +916%、vintage coffee corner +430%、Biscoff latte recipe +359%)が強い追い風として存在。
- Google検索：複数の実売中商品が独立に確認でき、テーマの継続的な存在が裏付けられる。

**なぜ伸びているか**：「お店（空間）」というモチーフは横展開しやすく、Amazon・Etsy双方で既に複数の独立商品が育っている＝市場参加者が需要を感知し続けている状態。加えてPinterestの「家でカフェ体験を演出する」トレンドが直接的な追い風になっている。

**購入者の欲求**：実際にカフェ・書店に行けない中での疑似体験。静かで落ち着いた空間への憧れ。「頑張らなくていい場所」としての癒やし。

**競合状況**：商品数は増えているが、大手ブランドによる寡占はまだ確認されない。中程度の競合。「Cozy Library」という派生が今後の差別化ポイントになりうる。

**AI生成適性**：高い。店内インテリア・什器・本棚・コーヒーカップなど反復要素が多い。

**表紙分析**：窓際の本棚とコーヒーカップ、丸まる猫の構図が定番化しつつある。暖色照明・太めの輪郭線を維持しつつ、「Library」派生では本の背表紙の密度を上げて差別化する余地あり。

**推奨判断：今すぐ作る**（継続。Cozy Libraryをシリーズの新フレーバーとして追加投入する好機）

---

### 2位：Cozy Kitchen Witch（コージー・キッチンウィッチ）

総合点：**85/100**(先週87)　Momentum：**45/100**　Confidence：**High**　Trend Stage：**3**(先週2)　判断：**今すぐ作る(BUILD_NOW)** ⚠️SATURATION ALERT

**市場状況**
- Amazon：「Cozy Kitchen Witch Coloring Book」「Kitchen Witch Coloring Book」「Cozy Witch Kitchen Coloring Book」「Magical Cooking Witch Coloring Book」「Coloring the Kitchen Witch」「Cozy Witchy Kitchens and Apothecaries」「The Cozy Witch's Kitchen」など**少なくとも7〜8点**の類似コンセプト商品を確認。先週から明確に増加。
- Etsy：「witchy kitchen」という複合語での集約marketページ(UK)を新たに確認。横ばい〜微増。
- Pinterest：公式Fall 2026 Hobbies Trend Reportで「Kitchen Witch」トレンドが確定・詳細化(+midnight margaritas +140%、+candle making tutorial +118%)。映画『Practical Magic 2』とのタイアップも継続。

**なぜ伸びているか**：Pinterest公式データと文化的トリガー(映画公開)が重なり続けている一方、**供給側(Amazonの競合商品)が需要確認から1週間で急増**しており、典型的な「ブルーオーシャン→競争激化」への移行局面に入った。

**購入者の欲求**：日常に小さな儀式感を取り入れたい。ハロウィン限定でない通年楽しめる魔女モチーフ。

**競合状況**：⚠️**SATURATION ALERT** — 先週「特化ニッチはまだ手薄」だった状態から、1週間で7〜8点の直接競合が確認される状態に変化。「短期間での類似商品急増」という設定基準に合致。今から参入する場合はサブニッチ（例：Sea Witch、Forest Witch等）での差別化が必須。

**AI生成適性**：高い。魔女+ハーブ瓶+猫+キッチン小物の組み合わせは安定生成しやすい。

**推奨判断：今すぐ作る**（ただし「Kitchen Witch」単体ではなくシリーズ展開の1フレーバー(季節/派生ライン)として即座に差別化ポイントを追加することを強く推奨）

---

### 3位：Analog Lifestyle / Digital-Detox Ritual Coloring（アナログ・ライフスタイル／デジタルデトックス儀式）

総合点：**83/100**(新規BUILD_NOW入り、先週はブルーオーシャン監視項目)　Momentum：**N/A(新規登録)**、ただし定性的モメンタムは非常に高い　Confidence：**Medium**　Trend Stage：**3**　判断：**今すぐ作る(BUILD_NOW)** 🚨VELOCITY ALERT

**市場状況**
- Amazon：「Digital Detox: Unplugged Life Coloring Book for Adults」「Digital Detox Coloring Book Series」「Digital Detox Unplugged Nature Escapes」「Digital Detox: An Adult Coloring Book to Disconnect from the World」「The Digital Detox Coloring Book and Journal」「Cozy Digital Detox Coloring Book」「Digital Detox Activity Book」など**7点**を確認。先週は「ほぼ皆無」と報告していたテーマが、実際には既に複数商品化されていたことが判明。
- Pinterest：**Fall 2026 Hobbies Trend Report全体のフレーミングが「スマホから離れる」であり、9トレンドの多くがアナログ回帰(手紙・ジン作り・押し花・刺繍・占星術)**。「Handmade Hacker」トレンドの一部としてdream journaling +128%。
- Google検索：「2026年=アナログの年」と明言する独立記事が複数(Planoly、Deseret News、HerCampus)。「ジャーナリングがプロダクティビティアプリの売上を上回っている」との報道。
- SNS：「2026 Journal Ecosystem」トレンド(用途別ノート使い分け)、アナログバッグ・紙の手帳の可視化が報告。

**なぜ伸びているか**：**確認市場数が実質1(先週：Amazonのみで少数商品)→4(Amazon・Pinterest・SNS・Google検索)に拡大**しており、`config/research-config.json`のVELOCITY ALERT例示基準「確認市場数が2→4以上に拡大」にほぼ合致する。塗り絵はもともと「手を動かすアナログ行為」そのものであり、業界横断のアナログ回帰の波に自然に乗れるポジションにある。

**購入者の欲求**：スマホ依存への罪悪感からの解放。「何も生産しない」ことへの許可。ジャーナリング・手帳文化との親和性。

**競合状況**：7点の競合が既に存在するが、まだ「Digital Detox」という単一ワードに集中しておらず、サブテーマ(ジャーナリング融合、自然逃避、儀式性)での差別化余地は大きい。BUILD_NOWとするが、Confidenceは**Medium**にとどめる(Etsy側での塗り絵特化の直接的裏付けがまだ弱いため、`config`の「スコアが高い＝確実ではない」原則に従いConfidenceを控えめに設定)。

**AI生成適性**：高い。手帳・ペン・キャンドル・観葉植物・窓辺などの静物モチーフはAIと相性が良い。

**表紙分析**：スマホをそっと伏せた手元、窓辺の手帳とペン、キャンドルの灯りといった「静けさ」を伝える構図。派手さより「間」を活かしたミニマルなレイアウトが効果的と推測される。

**推奨判断：今すぐ作る**（ただし小ロットでのテスト販売を推奨。Etsy側の反応を最優先で計測すること）

---

### 4位：Goblincore Coloring（ゴブリンコア）【新規】

総合点：**78/100**(新規)　Momentum：**N/A(新規)**　Confidence：**Medium**　Trend Stage：**2**　判断：**テストする(TEST)** 🚨VELOCITY ALERT

**市場状況**
- Etsy：「Goblincore Coloring Book: 25 Mystical Witchcraft Pages」「Goblincore Coloring Book | Witchy Magic Woods, Crystals」(50ページ級)など複数の独立バンドル出品、専用market集約ページも確認。**Etsy側が先行している疑いが強い**。
- Amazon：「Goblincore Coloring Book: Reject the Perfection and Embrace the Diversity and Curiosities of Nature」(Chartwell Books)を確認。件数はまだ少ない。
- Google検索・Google Trends：accio.com、paulamcnulty.com等複数の独立記事が2026年注目トレンドとして明示的に言及(「森の地面・苔・カタツムリ・カエル・忘れられたガラクタを愛でる」美学)。
- SNS：Mr Porter(ファッション誌)、alittlebithumanが「goblincoreはcottagecoreより暗く汚れている」と解説、TikTok discoverタグも複数存在。

**なぜ伸びているか**：Cottagecore Mushroom & Gardenの隣接ニッチだが、「完璧主義への反発」「不気味さ・雑然さの肯定」という独自のテーマ性を持ち、Z世代のデジタル疲れ・脱完璧主義志向と結びついている。**新規テーマが初登場でいきなり4市場(Etsy・Amazon・Google・SNS)から確認できる**のは異例で、VELOCITY ALERTに相当する。

**購入者の欲求**：「可愛くなくていい」自然への愛着。cottagecoreよりダークで大人びた世界観を求める層。

**競合状況**：Etsyでは複数出品があるがAmazon側はまだ薄い＝ブルーオーシャンに近い状態。

**AI生成適性**：高い。きのこ・苔・カエル・クリスタルなどの要素はAI生成と相性が良い。

**関連ステッカーテーマとの連携（重要）**：ステッカーモジュールの深掘り調査(`research/themes/stickers.json`の`sticker-goblincore-mushroom-frog`、2026-08-27更新)で、Goblincoreのサブセットである「Frog & Mushroom」テーマは既にConfidence=High・`product_decision: BOTH`(塗り絵・ステッカー両方に適する)と判定済み(`coloring_fit: 82`, `sticker_fit: 90`)。今回確認したGoblincoreはそれより広い世界観(苔・クリスタル・呪文書・ガラクタ集め等)を含むため、既存の`cottagecore-mushroom-garden`および`sticker-goblincore-mushroom-frog`とは別テーマとして独立管理しつつ、商品企画時は両者の重複(特にFrog & Mushroomモチーフ)を避けるよう次回精査すること。

**推奨判断：テストする**（新規テーマのため今回はTESTにとどめる。次回調査でAmazon側の伸びを最優先確認）

---

### 5位：Grayscale Photorealistic Nature & Animals（グレイスケール写実調）

総合点：**79/100**(先週76)　Momentum：**55/100**　Confidence：**Medium**　Trend Stage：**3**(先週2)　判断：**テストする(TEST)**

**市場状況**
- Amazon：「Grayscale Wildlife: Majestic Animals in Photorealistic Detail」の最新刊(2026-08-13出版)を確認。5冊構成のKindleシリーズとして展開中。「Realistic Animals Vintage Grayscale Mandala」等、grayscale×vintage/mandalaのハイブリッド化も進行。
- Etsy：継続して強い(40 Realistic Wildlife Animals Set等)。業界記事側でも「2026年最も急成長中のニッチ」という評価が複数回再登場。
- Pinterest：直接データはないが、Predicts 2026の「Wilderkind」(動物・自然モチーフ全体の追い風)が間接的に関連。

**なぜ伸びているか**：上級者・リピーター層が「簡単すぎる塗り絵」に飽き始め、より作品性の高い写実調にプレミアム価格で向かっているとの分析が今回も複数の独立ソースで一致。8月13日出版という直近実績が裏付けを強化。

**競合状況**：線画型より手薄だが、シリーズ展開(5冊)が進行中で先行者の優位性が固まりつつある。

**AI生成適性**：中程度(線画より品質管理が難しい)。

**推奨判断：テストする**（プレミアム価格帯・小ロットで検証を継続）

---

### 6位：Cottagecore Mushroom & Garden（コテージコア・きのこ＆ガーデン）

総合点：**75/100**(先週77)　Momentum：**35/100**　Confidence：**Medium**　Trend Stage：**4**(先週3)　判断：**テストする(TEST)** ⚠️SATURATION ALERT

**市場状況**：Amazonで**9点以上**を再確認、さらに増加傾向。Etsyでは「mushroomcore」という単独派生語が定着。Pinterest Fall Hobbies Trend Reportの新トレンド「Backyard Botanist」(押し花+457%、鳥スケッチ+232%)が隣接領域として追い風。

**競合状況**：⚠️既に高密度な競合ニッチであり、さらに競合が増加している。単独テーマとしての新規参入価値は下がりつつある。差別化には「きのこ×占星術(Goblincore寄り)」等のさらなる細分化が必要。

**関連ステッカーテーマ**：`sticker-goblincore-mushroom-frog`(BUILD_NOW/BOTH判定)と直接連携。塗り絵側も`coloring_fit`の観点で今後BOTH運用を検討する価値あり。

**推奨判断：テストする**（きのこ単体特化、または上位のGoblincoreとの統合企画で差別化）

---

### 7位：Bold & Easy Cute Animals（ボールド＆イージー・キュートアニマル、Axolotlサブニッチ含む）

総合点：**73/100**(先週74)　Momentum：**40/100**　Confidence：**Medium**　Trend Stage：**5**　判断：**テストする(TEST)** ⚠️SATURATION ALERT(継続)

**市場状況**：定番ジャンルとして継続活発。今週新たに、**Axolotl(アキソロトル)単体ニッチ**が「Amazon KDPで圧倒的な需要、競合は中程度」と複数の独立記事(kdpeasy.com経由、medium.com記事)で名指しされた。「特定の1動物に絞り込んだ方が、汎用的な『可愛い動物』塗り絵より売れる」という市場全体の傾向の代表例として挙げられている。

**推奨判断：テストする**（単独の汎用ジャンルとしては成熟済み。Axolotl等、単一動物への絞り込みを次の一手として検討）

---

### 8位：Capybara Cozy & Cottagecore（カピバラ×コージー）

総合点：**66/100**(先週79、大幅ダウン)　Momentum：**15/100**　Confidence：**Medium**　Trend Stage：**5**(先週3)　判断：**テストする(TEST)** ⚠️SATURATION ALERT + 需要頭打ちの疑い

**市場状況**
- Amazon：2026年を通じて新刊投入が継続(直近は8月11日出版のCoco Wyo作品)。**供給は衰えていない**。
- Google Trends(二次情報)：accio.comの記事が「カピバラバケットハット」のGoogle Trends検索は**2025年7月にピーク(100)、以降は目立った再燃データなし**と報告。
- SNS：「2026年のスピリット動物」との記事はあるが、直近の急上昇を示す一次データはなし。周期的なバイラル現象との分析あり(Dexerto)。

**なぜスコアを下げたか**：**「供給(新商品)は増え続けているのに、需要側の独立指標(検索トレンド)はむしろ1年以上前にピークアウトしている」という、典型的な後期飽和パターンの兆候**が今回複数市場で確認できたため、Opportunity Scoreを引き下げた。config記載のSATURATION ALERT基準「参入タイミングとして遅い可能性」に該当。

**推奨判断：テストする**（新規参入には慎重を要する。既存シリーズを持つ場合の横展開に限定するのが無難）

---

### 9位：Grandmacore Cottage Coloring（グランマコア）

総合点：**68/100**(先週85、大幅ダウン)　Momentum：**10/100**　Confidence：**Low**(変わらず)　Trend Stage：**1**(変わらず)　判断：**テストする(TEST)**　※先週のBUILD_NOWから格下げ

**市場状況**：Amazonで「Granny Chic Coloring Book」「Grandma Cottagecore Coloring Book」の2〜3点を確認したのみで、先週から**実質的な新規参入の増加なし**。Etsyでも「grandmacore」単体の塗り絵市場は依然として未確立(ホームデコア中心)。Pinterest側も今週は新規の公式数値更新なし(先週のSpring Trend Report数値のまま停滞)。

**なぜ格下げしたか**：先週のBUILD_NOW判定は「Pinterest公式データ(+545%/+915%)は強いが、Amazon/Etsyの実商品はほぼゼロ」という**仮説段階の例外的判断**だった。1週間経過しても実商品化がほとんど進んでいない(Amazon/Etsyでの動きが乏しい)ため、「需要はあるが商品化は追いついていない」という前回の楽観的解釈よりも、「この文言だけでは塗り絵という商品形態への需要転移がまだ実証されていない」という慎重な解釈に修正する。**機械的な足切りではなく、実際の追跡調査の結果としての格下げ**である。

**推奨判断：テストする**（小ロットでの実験は継続する価値があるが、優先度は下げる。次回調査でAmazon/Etsy側の動きが出るか要確認）

---

### 10位：Dark Academia Gothic Library（ダークアカデミア・ゴシック図書館）

総合点：**62/100**(先週68)　Momentum：**20/100**　Confidence：**Low**　Trend Stage：**4**(先週2、大幅上昇)　判断：**監視継続(WATCH)** ⚠️SATURATION ALERT(強)

**市場状況**：Amazonで**9点以上**を確認、先週からさらに増加。「Dark Academia Enchanted Library」「Gothic Academia: A Dark Arts Coloring Book」「Dark Academia & Gothic Libraries」など類似コンセプトが数ヶ月内に連続投入されている。Etsyでも「kawaii化」した派生が新たに出現(すでに二次分化が始まっている＝成熟シグナル)。Pinterest/SNSでの独立裏付けは今回も見つからず。

**なぜスコアを下げたか**：先週時点で既に「競合急増の兆候」を指摘していたが、今週の調査でそのペースが**さらに加速している**ことが確認された。Trend Stageを2→4に引き上げ(「競合急増」段階)、Opportunity Scoreを引き下げた。

**推奨判断：監視継続（実質的に見送り方向）**。低競争ニッチという評価はもはや過去のものになりつつあり、新規参入は推奨しない。

---

## WHAT CHANGED THIS WEEK

`scripts/compare-history.mjs`を、category="coloring"のみにフィルタした履歴ファイルで再実行した結果（詳細は上記セクション0参照、生のスクリプト出力をそのまま鵜呑みにせず、各エージェントの実地調査内容と突き合わせて採用）：

| テーマ | 先週スコア→今週スコア | 先週順位→今週順位 | 判定 |
|---|---|---|---|
| Cozy Cafe & Bookstore Series | 84→86 | 3位→1位 | 順位上昇、確認ソース数増加(velocity_candidate) |
| Cozy Kitchen Witch | 87→85 | 1位→2位 | 横ばい〜微減。Stage 2→3(競合急増によりスコアの伸びを相殺) |
| Analog Lifestyle/Digital-Detox Ritual Coloring | (ブルーオーシャン監視)→83 | 圏外→3位 | 新規登録(実質VELOCITY ALERT) |
| Goblincore Coloring | —→78 | 圏外→4位 | 新規登録(VELOCITY ALERT) |
| Grayscale Photorealistic Nature & Animals | 76→79 | 6位→5位 | 上昇 |
| Cottagecore Mushroom & Garden | 77→75 | 5位→6位 | 微減、Stage 3→4(飽和方向) |
| Bold & Easy Cute Animals | 74→73 | 7位→7位 | 横ばい |
| Capybara Cozy & Cottagecore | 79→66 | 4位→8位 | **下落**。Stage 3→5、需要頭打ちの疑い |
| Grandmacore Cottage Coloring | 85→68 | 2位→9位 | **大幅下落**。BUILD_NOW→TESTへ格下げ |
| Dark Academia Gothic Library | 68→62 | 8位→10位 | 下落。Stage 2→4、飽和加速 |
| Spooky Cute (Creepy-Cute) | 64→65 | 9位→11位(TOP10圏外) | 微増(季節要因)、AVOID継続 |
| Kawaii Original-Character Coloring | 60→58 | 10位→12位(TOP10圏外) | 微減、AVOID継続 |
| Old Money / Quiet Luxury Lifestyle Coloring | —→68 | 圏外→13位 | 新規登録(ブルーオーシャン候補として追跡開始) |

**消滅したテーマ**：なし（先週の塗り絵モジュール10テーマは全て今週も追跡対象として存続）。

---

## ブルーオーシャン候補（TOP10とは別枠、最低5個）

| テーマ | 兆候 | Amazon競合 | 他市場需要 | 総合判断 |
|---|---|---|---|---|
| Old Money / Quiet Luxury Lifestyle Coloring | Amazon独立2ブランド参入(「Cozy Old Money Life」「Glamour Queens」)、Quiet Luxuryファッション/ライフスタイルトレンドの波及 | 少ない(2点) | Etsy/Pinterest未確認(要フォローアップ) | 有望、次回優先調査 |
| Liminal Space / Backrooms / Weirdcore Coloring | Etsy複数独立出品(「Liminal Spaces Coloring Book」「Backrooms Coloring Book」「Not so Cozy Places」) | ほぼ皆無 | Z世代インターネット美学(weirdcore/dreamcore)由来、Amazon側は今回未検索 | ニッチだが独立需要あり、テスト候補 |
| Cosmic Reset(占星術・タロット・クリスタル) | Pinterest公式Fall Hobbies Trend Report: learn astrology +733%、crystals meanings +606%、tarot cards for beginners +558% | 未確認(既存の一般的タロット塗り絵は多いと推測されるが今回未検証) | Pinterest公式(高信頼度)、年次Predicts 2026とも方向性一致 | 商品化親和性が非常に高く優先調査推奨 |
| Backyard Botanist(押し花・ネイチャージャーナリング) | Pinterest公式: dried and pressed flowers +457%、bird drawing sketch +232% | 未確認 | Pinterest公式(高信頼度) | Cottagecore Mushroom/Grayscale Natureとの掛け合わせが有望 |
| Farmcore / Cozy Farm Animals Coloring | Etsy複数出品(「Cozy Farm Animals Coloring Pages: Bold and Easy」等) | 未確認(要調査) | Cottagecore隣接、Bold & Easy形式との親和性高 | Bold & Easyとの掛け合わせスタイルとして有望 |
| Axolotl単体ニッチ | 複数独立記事が「Amazon KDPで圧倒的需要、競合中程度」と明言 | 中程度(Bold & Easy Cute Animalsに包含される形で既存) | 未確認 | 単一動物特化の好例、次回優先調査 |

---

## Trend Radar

### 🔥 HOT NOW
- Cozy Cafe & Bookstore Series
- Cozy Kitchen Witch
- Spooky Cute / Creepy-Cute(季節要因、ハロウィン接近)

### 🚀 RISING
- Analog Lifestyle / Digital-Detox Ritual Coloring
- Goblincore Coloring
- Grayscale Photorealistic Nature & Animals
- Old Money / Quiet Luxury Lifestyle Coloring
- Cosmic Reset(占星術・タロット・クリスタル)
- Backyard Botanist
- Farmcore / Cozy Farm Animals
- Axolotl単体ニッチ

### 👀 WATCH
- Grandmacore Cottage Coloring(格下げ、実商品化待ち)
- Dark Academia Gothic Library(飽和加速)
- Liminal Space / Backrooms / Weirdcore
- Wilderkind(Pinterest年次トレンド、塗り絵化未確認)
- Curated Clutter(Pokémon等IP依存の疑いあり、要TRADEMARK CHECK)
- Coquette Coloring(ステッカー側では既にsaturation_alert=trueで格下げ済み、塗り絵側も慎重に扱う)
- Kawaii Original-Character Coloring
- Cryptid / Cryptozoology Coloring
- Weekend Equestrian / Handmade Hacker(Pinterest発、塗り絵化はこれから)

### 💀 DECLINING
- Capybara Cozy & Cottagecore(供給過多・需要頭打ちの兆候)
- Bold & Easy Cute Animals(単独ジャンルとしては完全に定番化・成熟、Axolotl等への細分化が必須)

---

## 商品企画（BUILD NOWテーマ全件）

### ① Cozy Cafe & Bookstore Series

先週(2026-08-26)作成した企画をベースに、今週判明した「Cozy Library」派生を反映して更新する。

**英語タイトル案×10**
1. Cozy Bookstore Coloring Book: Shelves, Cats & Candlelight
2. The Corner Café: A Bold & Easy Coloring Collection
3. Cozy Bakery: Sweet Treats Coloring Book for Grown-Ups
4. Rainy Day Reads: A Cozy Bookshop Coloring Book
5. Storefront Stories: Cafés, Bakeries & Bookstores Coloring Book
6. The Reading Nook: A Cozy Coloring Journey
7. Latte Art & Library Cats: A Cozy Café Coloring Book
8. Between the Shelves: A Bookstore Coloring Collection
9. **Cozy Library: A Coloring Book for Book Lovers**(今週の新発見を反映)
10. Pages & Pastries: A Cozy Coloring Book Duo

**サブタイトル案×5**
1. 40 Bold & Easy Designs for Book Lovers and Coffee Lovers
2. A Cozy Coloring Escape to Your Favorite Corner Café
3. Simple, Soothing Designs Featuring Books, Coffee & Comfort
4. Featuring Reading Nooks, Bakery Counters & Library Cats
5. Big, Easy-to-Color Designs for a Slow Sunday Afternoon

**表紙コンセプト×5**
1. 本棚の前でコーヒーを飲む猫　2. 窓際の読書スペースとブランケット　3. ショーケースに並ぶペイストリーとカフェカウンター　4. 雨の日の書店の入口、傘立てとベルの音　5. 積み上げた本とキャンドル、湯気の立つマグカップ

**中面アイデア×30**
本棚の全景／レジカウンターとレシート／読書中の猫／窓際の一人掛けソファ／コーヒー豆の麻袋／ペイストリーショーケース／古書の背表紙群／しおりコレクション／カフェの黒板メニュー／雨の日の窓ガラス／本を抱えた読者のシルエット／焼きたてクロワッサン／エスプレッソマシン／古い電球のペンダントライト／読書スタンプカード／小さな鉢植えの棚／古地図の壁掛け／ノートとペンのセット／ケーキスタンド／レコードプレイヤー／レトロなレジスター／本の山に埋もれた読書椅子／窓辺の多肉植物／カフェの外テラス席／傘立てとコート掛け／手書きのメニューボード／トートバッグと本／店の看板イラスト／夜の書店の灯り／**分厚い図書館の書架と梯子(Cozy Library新規)**

**シリーズ展開案×10**
1. Winter Holiday Edition　2. Spring Garden Café　3. Autumn Reading Edition　4. Mystery Novel Edition　5. Grayscale Deluxe Edition　6. Around the World Pastries　7. Kids' Bold & Easy Edition　8. Cat Café Bundle　9. Rainy Day Edition　10. **Cozy Library Edition(独立巻として今週追加)**

**検索キーワード**：Amazon: cozy bookstore coloring book, cozy café coloring, bakery coloring book adults, cozy library coloring book／Etsy: cozy cafe coloring pages, cozy bookshop coloring, bookish coloring page／Pinterest: cozy reading corner, home café aesthetic, cozy library aesthetic

**想定購入者**：20〜45歳、読書好き・カフェ好き・BookTok/BookTubeフォロワー

**購入理由**：疑似的な「理想の空間」体験、シリーズ化しやすく継続購入を促せる

**差別化ポイント**：「Cozy Library」という書架密度の高い派生を独立商品として先に出す(先週時点でAmazon上の確認は1点のみ)

**NG案**：特定の実在書店・カフェチェーンのロゴ・内装を模倣しない

---

### ② Cozy Kitchen Witch

先週の企画をベースに、競合急増を踏まえた差別化案を追加する。

**英語タイトル案×10**（先週案を維持、9番目を差別化案に更新）
1. Cozy Kitchen Witch: A Hygge Herbal Coloring Book
2. The Witch's Pantry: Bold & Easy Coloring for Cozy Witches
3. Herbal Apothecary: Potions, Plants & Cozy Spells Coloring Book
4. Witch Cats in the Kitchen: A Cozy Coloring Collection
5. Autumn Witch Kitchen: Grayscale Botanical Coloring Book
6. Cottage Witch: A Cozy Coloring Book for Grown-Ups
7. Spellbook & Tea: Cozy Witch Coloring for Relaxation
8. The Herbalist's Kitchen: Bold & Easy Witch Coloring Book
9. **Sea Witch's Galley: A Cozy Coastal Witch Coloring Book**(差別化案、今週追加)
10. Brew & Bloom: Herbal Witch Coloring Book for Adults

**サブタイトル案×5**（先週と同一）
1. 40 Bold & Easy Designs for Relaxation and Stress Relief
2. A Cozy Coloring Journey Through Herbs, Spells & Kitchen Magic
3. Simple, Soothing Designs for Witches Who Love Tea and Tranquility
4. Featuring Potion Bottles, Familiar Cats & Autumn Herbs
5. Perfect for Beginners: Big, Easy-to-Color Designs

**表紙コンセプト×5**（先週と同一、詳細は`research/reports/2026-08-26-trend-report.md`参照）

**中面アイデア×30**（先週の30案を維持。詳細は8/26レポート参照。追加候補：「魔女猫が窓辺で薬草を見張る」「Kitchen Witch専用のスパイスラック」）

**シリーズ展開案×10**（先週の10案を維持。**優先順位を変更**し、「Sea Witch Edition」「Forest Witch Edition」を最優先の差別化ラインとする＝競合が集中している「Kitchen」単体から離れたフレーバーを急ぐ）

**検索キーワード**：cozy witch coloring book, kitchen witch coloring, herbal apothecary coloring book, sea witch coloring book(新規), witchy kitchen coloring(Etsy集約語)

**想定購入者・購入理由**：先週と同一（`research/reports/2026-08-26-trend-report.md`参照）

**差別化ポイント**：「Kitchen」から離れたサブニッチ（Sea Witch、Forest Witch）への早期展開が最重要

**NG案**：特定の映画・小説のキャラクターデザインを模倣しない（『Practical Magic』のキャラクター自体の肖像模写は避け、あくまで「魔女×キッチン」という一般的モチーフにとどめる）

---

### ③ Analog Lifestyle / Digital-Detox Ritual Coloring（新規BUILD_NOW、フル新規企画）

**英語タイトル案×10**
1. Digital Detox: A Cozy Coloring Ritual for Unplugging
2. Offline Hours: A Slow Coloring Journal for Screen-Free Living
3. Put the Phone Down: Bold & Easy Coloring for a Calmer Mind
4. Analog Afternoons: A Coloring Book for Unplugged Living
5. The Unplugged Journal: Coloring, Reflection & Quiet Rituals
6. Screen-Free Sundays: A Cozy Coloring & Journaling Book
7. Slow Living Rituals: An Analog Coloring Book for Adults
8. Tea, Ink & No Notifications: A Digital Detox Coloring Book
9. The Quiet Hour: Coloring Pages for Disconnecting
10. Handwritten & Hand-Colored: An Analog Life Coloring Book

**サブタイトル案×5**
1. 40 Bold & Easy Designs to Help You Disconnect and Recharge
2. A Cozy Coloring Companion for Screen-Free Evenings
3. Simple, Soothing Pages for Slowing Down and Being Present
4. Featuring Journals, Candles, Tea Rituals & Quiet Corners
5. Big, Easy-to-Color Designs for a Calmer, Analog Life

**表紙コンセプト×5**
1. 伏せられたスマートフォンの横に開かれた手帳とペン
2. 窓辺のキャンドルとお茶、閉じたノートパソコン
3. ハンモックで本を読む人物のシルエット、遠くの電子機器は描かない
4. 押し花とインク瓶、手紙を書く手元のクローズアップ
5. 観葉植物に囲まれた読書スペース、時計だけが時間を示すミニマルな構図

**中面アイデア×30**
開いた手帳とペン／ハーブティーのカップ／キャンドルの灯り／窓辺の観葉植物／押し花のしおり／万年筆とインク瓶／手紙を書く手元／古いカメラ(フィルム式)／レコードプレイヤー／編みかけの毛糸／ハンモックでの読書／庭の散歩道／星空を見上げる人影／手帳のデコレーションページ／ジャーナリングの道具一式／散らかった机の上の紙とペン／窓の外の景色をスケッチする手元／お風呂とキャンドル／朝のコーヒーとノート／自然の中でのピクニック／手作りのジン(コラージュ)ページ／タロットカードと静かな読書灯／植物を観察してスケッチする様子／ヨガマットと朝の光／手紙を封筒に入れる手元／古い地図を広げるテーブル／ドライフラワーのリース作り／手編みのマフラー／窓辺で編み物をする人影／時計のない部屋のイメージ

**シリーズ展開案×10**
1. Digital Detox: Morning Rituals Edition　2. Digital Detox: Evening Wind-Down Edition　3. Digital Detox: Nature Escape Edition　4. Digital Detox: Journaling Companion Edition　5. Digital Detox: Tea & Tarot Edition(Cosmic Resetとのクロスオーバー)　6. Digital Detox: Grayscale Deluxe Edition　7. Digital Detox: Travel-Size Pocket Edition　8. Digital Detox: Kids' Bold & Easy Edition　9. Digital Detox: Seasonal Almanac Edition　10. Digital Detox: Letter-Writing Companion Edition

**想定購入者**：25〜45歳、SNS疲れ・燃え尽き症候群を自覚している層、ジャーナリング・手帳文化のフォロワー

**購入理由**：スマホ依存への罪悪感の解消、「何も生産しなくていい」時間への許可、アナログな手作業への回帰欲求

**検索キーワード**：Amazon: digital detox coloring book, unplugged coloring book, analog lifestyle coloring／Etsy: digital detox journal printable, screen free coloring page／Pinterest: digital detox aesthetic, analog lifestyle, off your phone ritual

**差別化ポイント**：既存7点の競合の多くが「デジタルデトックス」を主題として明示しているが、「ジャーナリング融合」「タロット/占星術融合(Cosmic Reset連携)」といった具体的な生活儀式との掛け合わせで差別化する

**NG案**：スマホやSNSブランドを否定的に揶揄する過度に説教的なトーンは避け、あくまで「癒やし」のポジティブな提案に留める

---

## DATA QUALITY REPORT

**成功ソース**：WebSearchによる全6市場(Amazon/Etsy/Pinterest/Google Trends/SNS/Google検索)の検索結果スニペット取得はすべて成功。Pinterest公式Fall 2026 Hobbies Trend Report、Pinterest Predicts 2026という価値の高い一次情報の存在をWebSearch経由で特定できた。

**失敗ソース**：
- `amazon.com`, `etsy.com`, `pinterest.com`(および`newsroom.pinterest.com`), `trends.google.com`, `tiktok.com`への直接WebFetchは全件`EGRESS_BLOCKED`。
- 一般ブログ・ニュースサイトの一部(`kdpeasy.com`, `coloringbook.dev`, `coloringqueen.net`, `nssmag.com`, `moneywise.com`, `shopping.yahoo.com`等)も今回はWebFetchがブロックされ、WebSearch要約のみに依存。

**欠損データ**：BSR・レビュー数・星評価・Etsyの販売数/お気に入り数・Google Trendsの生グラフ・TikTok/Instagramの再生数やエンゲージメント率は、今回も一切取得できなかった。すべて定性的な「独立出品/商品の存在数」を主な判断材料とした。

**分析への影響**：数値的な検証ができないため、Confidenceは全体的に保守的(Medium以下中心)に設定した。特にAnalog Lifestyle/Digital-Detox Ritual ColoringはOpportunity Scoreが高い一方、Confidenceは意図的にMediumに抑えている。

**インフラ上の既知の問題(申し送り事項)**：`scripts/compare-history.mjs`が`trend-history.json`内の`category`(coloring/sticker)を区別せずに「直近の日付」を選択するため、片方のモジュールしか実行しない週には誤った基準日と比較してしまう。今回は手動でcategoryフィルタ済みの一時履歴ファイルを作成して回避したが、次回以降のためにスクリプト自体へ`--category`オプションを追加することを推奨する。

**先週の自動実行の不具合について**：2026-08-31分の自動実行(GitHub Actions, run #33360353072)は「成功」ステータスを返しながら実際には調査・保存・コミットを一切行わないという不具合が発生し、`scripts/validate-output.mjs`によって検出・失敗表示された。本レポートはユーザーの依頼により手動で埋め合わせたものであり、自動実行側の根本原因調査は別途対応予定（本セッションでは着手していない）。
