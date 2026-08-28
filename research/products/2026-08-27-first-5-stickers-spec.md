# 最初の5商品 制作仕様書(ステッカー)

作成日: 2026-08-27
対象: Priority 1(Frog & Mushroom / Cottagecore/Goblincore)3点 + Priority 2(Book Club Stickers)2点
参照元: `research/reports/2026-08-27-sticker-weekly-report.md`「THIS WEEK'S BUILD LIST」、
`research/themes/stickers.json`(theme_id: `sticker-goblincore-mushroom-frog`, `sticker-book-club-poetcore`)

この仕様書のGeminiプロンプトは**英語のまま**Geminiの画像生成(Gemini/Imagen)に貼り付けて使用できます。
文章内の説明・注意事項は日本語で記載しています。

---

## 0. 共通スタイルガイド(5商品すべてに適用)

ショップ全体の世界観を統一するため、以下をすべてのプロンプトに共通指定しています。

- **画風**: フラットベクターイラスト、太めの黒アウトライン、グラデーションなし、影は最小限のソフトシェーディングのみ
- **背景**: 純白(#FFFFFF)背景に単体被写体を配置(背景除去・ダイカット加工をしやすくするため)
- **構図**: 中央配置、単一モチーフ、テキスト・ウォーターマークなし
- **アスペクト比**: 正方形 1:1
- **色数**: 各デザインにつき3〜4色程度に抑え、シリーズとしての統一感を出す

### 生成後の共通作業手順
1. Geminiでプロンプトを実行し、白背景の画像を生成
2. 背景除去ツール(remove.bg、Photoshopの被写体選択等)で透過PNG化
3. ダイカットステッカーとして印刷する場合は、アウトラインの外側に白フチ(2〜3mm相当)を残すこと
4. ファイル名は下記の「ファイル名」欄に従うこと(例: `frog-mushroom-umbrella-01.png`)
5. Etsy/Amazon出品時は各商品の「Etsyキーワード」を商品タイトル・タグに反映する

### IPリスク回避の共通ルール(重要)
- **カエルのデザイン全般(商品1・3)**: サンリオ「ケロッピ」を想起させる、丸く大きな漫画的な目・赤白ストライプの服・パステルグリーンの組み合わせは**使用しないこと**。プロンプトには "NOT cartoon character eyes, no clothing" を明記済み
- **本のデザイン(商品4)**: 実在する書籍の表紙デザイン・タイトル文字を描かせないこと。プロンプトには "No visible text or titles on the book spines" を明記済み
- **商品名・タグに使わない語**: 「BookTok」「Silent Book Club」(いずれも登録商標)。本仕様書のタイトル案では使用していません

---

## 商品1: Frog Under a Mushroom Umbrella(カエルのきのこ傘宿り)

**由来テーマ**: Frog & Mushroom(Cottagecore/Goblincore) — Priority 1 / theme_id: `sticker-goblincore-mushroom-frog` / sub_niche: `cottagecore-frog`
**コンセプト**: 小さなカエルが大きな赤いきのこの傘の下で雨宿りしているシーン。コテージコアの定番モチーフの中でも今回最もエビデンスが強い組み合わせ。

| 項目 | 内容 |
|---|---|
| 商品タイプ | Die-cut vinyl sticker(耐水ビニールステッカー)+ Digital sticker兼用 |
| サイズ目安 | 7.5cm × 7.5cm(3×3インチ)相当 |
| カラーパレット | フォレストグリーン(蛙)、クリーム(お腹)、深紅+白ドット(きのこ傘)、暖褐色(地面) |
| ファイル名 | `frog-mushroom-umbrella-01.png` |
| Etsyキーワード | cottagecore frog sticker, frog mushroom sticker, cute toad sticker |
| Pinterestキーワード | cottagecore frog aesthetic, frogcore |

**Geminiプロンプト(コピー用)**
```
A cute die-cut sticker illustration of a small toad-like frog sheltering under a large red-and-white spotted toadstool mushroom, as if using it as an umbrella. Cottagecore, whimsical storybook style. The frog has a rounded, naturalistic amphibian body with simple small oval eyes (NOT big cartoon character eyes, no clothing, no anthropomorphic accessories) in warm olive-green with a cream belly, sitting on a small patch of moss with tiny white flowers. The mushroom cap is deep red with white spots, warm brown stem. Flat vector illustration, clean bold black outlines, soft minimal cel-shading only, no gradients. Centered composition, single subject, isolated on a solid pure white background, square 1:1 aspect ratio, no text, no watermark, high resolution, print-ready sticker art.
```

---

## 商品2: Mushroom Cottage with Snail(きのこの家とカタツムリ)

**由来テーマ**: Frog & Mushroom(Cottagecore/Goblincore) — Priority 1 / theme_id: `sticker-goblincore-mushroom-frog` / sub_niche: `frog-and-mushroom-general`(親カテゴリの中面アイデアより)
**コンセプト**: きのこの根元に建てられた小さな家。蔦と苔、玄関先にカタツムリ。カエル不使用のためIPリスクは最小。

| 項目 | 内容 |
|---|---|
| 商品タイプ | Die-cut vinyl sticker + Digital sticker兼用 |
| サイズ目安 | 7.5cm × 7.5cm(3×3インチ)相当 |
| カラーパレット | 深紅(きのこ屋根)、暖褐色(木の扉)、黄色味の光(窓)、モスグリーン(苔) |
| ファイル名 | `mushroom-cottage-snail-01.png` |
| Etsyキーワード | mushroom cottage sticker, goblincore house sticker, cottagecore fairy house |
| Pinterestキーワード | mushroom cottage aesthetic, fairycore cottage |

**Geminiプロンプト(コピー用)**
```
A whimsical die-cut sticker illustration of a tiny cottage built into the base of a large mushroom, with a round wooden door and a small window glowing warm yellow, moss and small vines growing on the roots below, a friendly snail with a spiral shell resting on the doorstep. Cottagecore fairycore style. Warm autumn color palette of deep red mushroom cap, brown wood, warm yellow window light, and moss green. Flat vector illustration, clean bold black outlines, soft minimal shading, no gradients. Centered single-subject composition, isolated on a solid pure white background, square 1:1 aspect ratio, no text, no watermark, print-ready sticker art.
```

---

## 商品3: Frog with Berry Basket(ベリーかごを運ぶカエル)

**由来テーマ**: Frog & Mushroom(Cottagecore/Goblincore) — Priority 1 / theme_id: `sticker-goblincore-mushroom-frog` / sub_niche: `mushroom-frog`
**コンセプト**: 小さなカエルが編みかごにベリーを摘んで運んでいる。頭に小さな花冠。商品1とセットで「森の生き物の暮らし」シリーズとして展開しやすい。

| 項目 | 内容 |
|---|---|
| 商品タイプ | Die-cut vinyl sticker + Digital sticker兼用 |
| サイズ目安 | 7.5cm × 7.5cm(3×3インチ)相当 |
| カラーパレット | モスグリーン(蛙)、ベリーレッド、蜂蜜色(かご)、白い小花 |
| ファイル名 | `frog-berry-basket-01.png` |
| Etsyキーワード | cottagecore frog sticker, frog basket sticker, forest frog aesthetic |
| Pinterestキーワード | cottagecore frog, wilderkind aesthetic |

**Geminiプロンプト(コピー用)**
```
A cute die-cut sticker illustration of a small naturalistic frog with simple small oval eyes (NOT big cartoon character eyes, no clothing) standing upright in a gentle storybook pose, carrying a small woven wicker basket filled with red berries, wearing a tiny crown of small white wildflowers around its head. Cottagecore whimsical style. Warm color palette of moss green, berry red, and honey brown. Flat vector illustration, clean bold black outlines, soft minimal shading, no gradients. Centered composition, isolated on a solid pure white background, square 1:1 aspect ratio, no text, no watermark, print-ready sticker art.
```

---

## 商品4: Stack of Books with Reading Glasses(積み本と丸メガネ)

**由来テーマ**: Book Club Stickers — Priority 2 / theme_id: `sticker-book-club-poetcore` / sub_niche: `book-club`
**コンセプト**: 積み上げた本と丸メガネ、リボンのしおり。「book club stickers +243%」の中核サブニッチに対応する、最も汎用性の高いデザイン。

| 項目 | 内容 |
|---|---|
| 商品タイプ | Die-cut vinyl sticker + Digital sticker兼用 |
| サイズ目安 | 7.5cm × 7.5cm(3×3インチ)相当 |
| カラーパレット | セージグリーン、ダスティローズ、クリーム、テラコッタ(本の表紙、無地) |
| ファイル名 | `book-stack-glasses-01.png` |
| Etsyキーワード | book club stickers, bookish sticker, reading journal sticker |
| Pinterestキーワード | book club aesthetic, bookish stationery |

**Geminiプロンプト(コピー用)**
```
A cozy die-cut sticker illustration of a stack of four hardcover books in muted sage green, dusty rose, cream, and terracotta, with a pair of round vintage reading glasses resting on top and a small ribbon bookmark hanging from between the pages. Poetcore bookish aesthetic, warm and inviting. The book covers are plain solid colors with no visible text, titles, or logos. Flat vector illustration, clean bold black outlines, soft minimal shading, no gradients. Centered composition, isolated on a solid pure white background, square 1:1 aspect ratio, no text, no watermark, print-ready sticker art.
```

---

## 商品5: Fountain Pen & Pressed Flower(万年筆と押し花)

**由来テーマ**: Book Club Stickers(Poetcore的アクセントデザイン) — Priority 2 / theme_id: `sticker-book-club-poetcore` / 関連: `sticker-poetcore-stationery`(TEST判定テーマの意匠を、実測データのあるBook Clubパック内の1デザインとして低リスクに取り込む形)
**コンセプト**: 万年筆とインクの染み、押し花。Book Clubパックの中に1枚加えることで、Poetcore世界観を仮説段階のまま単独商品化せずに市場テストできる。

| 項目 | 内容 |
|---|---|
| 商品タイプ | Die-cut vinyl sticker + Digital sticker兼用 |
| サイズ目安 | 6cm × 6cm(2.5×2.5インチ)相当(他4点よりやや小ぶりなアクセントデザイン) |
| カラーパレット | バーガンディ(ペン)、セピアブラウン、ダスティラベンダー(花) |
| ファイル名 | `fountain-pen-pressed-flower-01.png` |
| Etsyキーワード | poetcore stickers, fountain pen sticker, literary aesthetic sticker |
| Pinterestキーワード | poet aesthetic, poetcore |

**Geminiプロンプト(コピー用)**
```
A delicate die-cut sticker illustration of a vintage fountain pen resting diagonally beside a small pressed lavender flower and a tiny circular ink blot, in a poetcore literary aesthetic. Muted color palette of deep burgundy pen, sepia brown ink, and dusty lavender flower. Flat vector illustration, clean bold black outlines, soft minimal shading, no gradients. Centered composition, isolated on a solid pure white background, square 1:1 aspect ratio, no text, no watermark, print-ready sticker art.
```

---

## まとめ表

| # | 商品名 | 由来テーマ | サイズ | ファイル名 |
|---|---|---|---|---|
| 1 | Frog Under a Mushroom Umbrella | Frog & Mushroom(P1) | 3×3in | frog-mushroom-umbrella-01.png |
| 2 | Mushroom Cottage with Snail | Frog & Mushroom(P1) | 3×3in | mushroom-cottage-snail-01.png |
| 3 | Frog with Berry Basket | Frog & Mushroom(P1) | 3×3in | frog-berry-basket-01.png |
| 4 | Stack of Books with Reading Glasses | Book Club(P2) | 3×3in | book-stack-glasses-01.png |
| 5 | Fountain Pen & Pressed Flower | Book Club(P2)/Poetcore | 2.5×2.5in | fountain-pen-pressed-flower-01.png |

商品1〜3で「森の生き物の暮らし」ミニシリーズ、商品4〜5で「Book Club」パックの中核2デザインを構成します。
生成・背景除去が終わったら、`research/products/` 配下に完成画像を追加し、この仕様書のファイル名と一致させて管理してください。
