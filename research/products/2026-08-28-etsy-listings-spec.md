# Etsy出品仕様書 — Frog & Mushroom系 / Bookish系(Vol.1)

作成日: 2026-08-28
対象: `research/products/` の5点のステッカー画像(背景透過・白フチ済み)を2つのEtsy出品に分割
参照元: `research/products/2026-08-27-first-5-stickers-spec.md`、
`research/themes/stickers.json`(theme_id: `sticker-goblincore-mushroom-frog`, `sticker-book-club-poetcore`)

> タイトル・タグ・説明文は実際のEtsy出品で使う**英語**で記載しています(文字数制限はスクリプトで検証済み:
> タイトル127字・118字<140字、タグは全13個とも20字以内)。日本語は解説用です。
> 各出品は**3点/2点だけの小規模な"Vol.1"テストパック**という位置づけです
> (本来の推奨テスト数量は12〜20点でしたが、まず少数で市場反応を見る方針に合わせています)。

---

## Listing 1: Frog & Mushroom Cottagecore Sticker Pack

**収録デザイン(3点)**
1. Frog Under a Mushroom Umbrella(`frog-mushroom-umbrella-01.png`)
2. Mushroom Cottage with a Snail(`mushroom-cottage-snail-01.png`)
3. Frog with a Berry Basket(`frog-berry-basket-01.png`)

### 商品タイトル(127字)
```
Cottagecore Frog & Mushroom Stickers | Cute Vinyl Sticker Pack for Laptop Water Bottle Journal | Waterproof Goblincore Set of 3
```

### 説明文
```
Bring a little woodland magic to your everyday things. This set of 3 cottagecore-style vinyl stickers features a shy toad sheltering under a toadstool umbrella, a cozy mushroom cottage with a snail neighbor, and a flower-crowned frog gathering wild berries.

WHAT'S INCLUDED (3 designs)
- Frog Under a Mushroom Umbrella
- Mushroom Cottage with a Snail
- Frog with a Berry Basket

DETAILS
- Approx. 3 x 3 in (7.5 x 7.5 cm) each
- Premium matte vinyl, waterproof & UV-resistant
- Dishwasher-safe, made to last on water bottles, laptops, journals & more
- Ships as individual die-cut stickers, not a sheet

PERFECT FOR
Water bottles, laptops, journals, planners, or as a gift for anyone who loves frogs, mushrooms, and all things cottagecore.

This is Volume 1 of our growing Frog & Mushroom collection — more woodland friends are on the way. Message us if you'd like to see a specific design next!
```

### タグ(13個、各20字以内)
```
cottagecore frog, frog sticker pack, mushroom sticker, cute frog sticker, goblincore sticker,
cottagecore sticker, waterproof sticker, vinyl sticker pack, woodland sticker, fairycore sticker,
kawaii frog sticker, mushroom cottage, frog and mushroom
```

### サムネイル構成(Photo 1〜5)
| # | 内容 |
|---|---|
| Photo 1(サムネイル/検索結果に表示) | 3点を三角構図でウッド調の台の上にフラットレイ配置。苔・小さな野花・本物っぽい小さいきのこを脇に添え、柔らかい自然光。**検索一覧で他のカエル/きのこステッカーと並んでも視認性が高いよう、背景を暗すぎず・散らかりすぎない程度に** |
| Photo 2 | 3デザインの個別クローズアップを1枚にコラージュ(3分割グリッド) |
| Photo 3 | 水筒に貼った状態のライフスタイルモックアップ |
| Photo 4 | サイズ比較(定規または手のひらの上に置いた写真) |
| Photo 5 | ノート/ジャーナルの角に貼った状態 |

**Photo 1用 Geminiプロンプト(コピー用)**
```
A cozy overhead flat-lay product photography shot of three cottagecore-style die-cut vinyl stickers (a frog under a mushroom umbrella, a mushroom cottage with a snail, and a frog carrying a berry basket) arranged in a pleasing triangular composition on a rustic wooden table, surrounded by small props: a sprig of moss, a few tiny wildflowers, one real small mushroom, and a wicker basket with berries. Soft natural window light from the left, warm and inviting color grading, shallow depth of field with the stickers in sharp focus. Square 1:1 aspect ratio, no text, no watermark, high resolution, Etsy product photography style.
```

### 価格テスト案
| ラウンド | 価格 | 1点あたり換算 | 想定期間 |
|---|---|---|---|
| A(初期・低め) | **$8.99** | 約$3.00 | 出品〜2週間(初動の販売実績・レビューを稼ぐ) |
| B(中間) | **$10.99** | 約$3.66 | 3〜4週目 |
| C(高め) | **$13.99** | 約$4.66 | 5〜6週目、Aで一定の販売実績が付いてから |

**テスト方法**: Etsyは同一出品内での同時A/Bテストができないため、**同じ出品の価格を数週間ごとに順番に変更**して比較する方式を推奨します(出品を複製して同時比較する方法もありますが、レビュー・SEO評価が分散するため小規模ショップには非推奨)。各ラウンドで以下を記録してください: 閲覧数(Views)→お気に入り数(Favorites)→カート追加→購入数、および閲覧→購入の転換率。**最初の2週間は低価格帯からスタート**し、初期の販売実績・レビューを優先することをおすすめします(Etsyの検索順位は販売実績にも影響されるため)。

---

## Listing 2: Book Club Sticker Pack (Poetcore)

**収録デザイン(2点)**
1. Stack of Books with Reading Glasses(`book-stack-glasses-01.png`)
2. Fountain Pen & Pressed Flower(`fountain-pen-pressed-flower-01.png`)

### 商品タイトル(118字)
```
Book Club Sticker Pack | Bookish Vinyl Stickers for Laptop Journal Planner | Cute Reading & Poetcore Stickers Set of 2
```

### 説明文
```
For everyone who's happiest with a book in hand. This set of 2 cozy vinyl stickers features a stack of well-loved books topped with round reading glasses, and a vintage fountain pen resting beside a pressed lavender flower.

WHAT'S INCLUDED (2 designs)
- Stack of Books with Reading Glasses
- Fountain Pen & Pressed Flower

DETAILS
- Approx. 3 x 3 in (7.5 x 7.5 cm) — book design
- Approx. 2.5 x 2.5 in (6 x 6 cm) — fountain pen design
- Premium matte vinyl, waterproof & UV-resistant
- Dishwasher-safe, made to last on water bottles, laptops, journals & more
- Ships as individual die-cut stickers, not a sheet

PERFECT FOR
Book club nights, reading journals, planners, laptops, or as a gift for the reader in your life.

This is Volume 1 of our Book Club collection — more bookish designs coming soon. Tell us what you'd like to see next!
```

### タグ(13個、各20字以内)
```
book club sticker, bookish sticker, reading sticker, poetcore sticker, book lover sticker,
fountain pen sticker, reading journal, bookish stationery, cute book sticker, literary sticker,
book stack sticker, vinyl sticker pack, planner sticker
```

> **注意**: 「BookTok」「Silent Book Club」は登録商標のため、タイトル・タグ・説明文のいずれにも使用していません(`research/themes/stickers.json`のtrademark_check_required_phrases参照)。

### サムネイル構成(Photo 1〜5)
| # | 内容 |
|---|---|
| Photo 1(サムネイル) | 2点をリネン素材の布の上にフラットレイ配置。本物のティーカップ、小さな花瓶に活けたラベンダー(ドライ)、開いたノートを脇に添える。セージグリーン×ダスティローズの落ち着いた配色で統一 |
| Photo 2 | 2デザインの個別クローズアップ(横並び2分割) |
| Photo 3 | ノートPCの角に貼った状態のライフスタイルモックアップ |
| Photo 4 | サイズ比較(定規または手のひらの上) |
| Photo 5 | 読書ジャーナル・プランナーに貼った状態 |

**Photo 1用 Geminiプロンプト(コピー用)**
```
A cozy overhead flat-lay product photography shot of two poetcore-style die-cut vinyl stickers (a stack of books with reading glasses, and a fountain pen beside a pressed lavender flower) arranged on a linen tablecloth beside a real cup of tea, a small vase with dried lavender, and an open notebook. Soft natural window light, warm muted color palette of sage green, dusty rose, and cream. Square 1:1 aspect ratio, no text, no watermark, high resolution, Etsy product photography style.
```

### 価格テスト案
| ラウンド | 価格 | 1点あたり換算 | 想定期間 |
|---|---|---|---|
| A(初期・低め) | **$6.99** | 約$3.50 | 出品〜2週間 |
| B(中間) | **$8.99** | 約$4.50 | 3〜4週目 |
| C(高め) | **$10.99** | 約$5.50 | 5〜6週目、Aで一定の販売実績が付いてから |

2点セットのためListing 1より少し低い価格帯からスタートします。テスト方法・記録項目はListing 1と同様です。

---

## 共通の運用メモ

- 両出品とも「Vol.1」「Set of 2/3」を明記し、後から追加デザインを出せる余地を残しています(将来デザインが増えたら、新しい出品を作るか、既存出品の商品バリエーションとして追加するか、Etsyでの販売実績を見てから判断してください)
- 価格テストの結果(閲覧数・お気に入り数・転換率・実際の価格)は、記録できる形で残しておくと、将来Obsidian連携時に`Products/`ノートへそのまま移行できます。現時点ではこのファイルに追記するか、簡単なメモとして残しておくことを推奨します
- サムネイル用Geminiプロンプトは商品写真(モックアップ)用です。ステッカー本体のデザイン自体は`research/products/`の5点のPNGをそのまま使用してください
