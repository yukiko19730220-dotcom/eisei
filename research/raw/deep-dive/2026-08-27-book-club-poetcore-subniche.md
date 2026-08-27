# Book Club & Poetcore サブニッチ深掘り検証 — 2026-08-27

ユーザー指示による追加検証。「book club stickers +243%」を複数市場で裏取りし、10サブニッチに分解評価。

## 事実(Fact)と仮説(Hypothesis)の分離

### 事実
| # | 指標 | 数値 | 出典 | 対象 |
|---|---|---|---|---|
| F1 | "book club stickers"検索 | **+243%** | Pinterest Summer Trend Report 2025([wavy.com](https://www.wavy.com/news/national/pinterests-summer-2025-trend-report-books-clubs-are-in/), [bookriot](https://bookriot.com/pinterest-reveals-gen-zs-bookish-interests-this-summer/)) | Book Club |
| F2 | "book club crafts"検索 | +558% | 同上 | Book Club |
| F3 | "book club invitations"検索 | +173% | 同上 | Book Club |
| F4 | "book club hosting"検索 | +87% | 同上 | Book Club |
| F5 | "the poet aesthetic"検索 | +175% | Pinterest Predicts 2026([sourcingjournal](https://sourcingjournal.com/denim/denim-trends/pinterest-predicts-80s-maximalism-lace-poetcore-circus-2026-1234792760/)) | **Poetcore(アパレル文脈、ステッカーの数値ではない)** |
| F6 | "poet core"検索 | +75% | 同上 | Poetcore(同上) |
| F7 | "BookTok" | 米国登録商標(登録番号7989376、ByteDance/TikTok Ltd.、2025-10-21登録) | [Trademarkia](https://www.trademarkia.com/booktok-97980756) | フレーズ商標懸念 |
| F8 | "Silent Book Club®" | USPTO登録商標(登録番号5798692) | [silentbook.club](https://silentbook.club/pages/about-us) | Book Club |
| F9 | "Hot Girls Read"商標出願がコミュニティ反発で撤回された事例 | ブランドがブッキッシュスラング商標化を試み炎上→撤回 | 検索結果より | フレーズ系全般への警鐘 |
| F10 | Dark Academiaは既にステッカーモジュールで検出済み | stickers.json: opportunity_score 79, TEST, saturation_alert true | 社内データ | Dark Academia |
| F11 | Etsyに主要サブニッチ全てで独立market pageが存在 | WebSearch確認(本文未取得) | 全サブニッチ |
| F12 | Amazonにも"Book Club Stickers"専用検索結果ページが存在 | [Amazon](https://www.amazon.com/Book-Club-Stickers/s?k=Book+Club+Stickers) | Book Club |

### 仮説(Hypothesis)
- H1: F5/F6とF1が世界観として隣接するため、Poetcoreもステッカー需要として伸びる可能性がある(推測、実測値ではない)
- H2: "Book Club Night"は独立トレンドとして確認できず、Book Clubの意匠バリエーションである可能性が高い(仮説)
- H3: "Literary Girl"はDark Academia/Dark Romance/Poetcoreと重複する消費者層を指す仮説的な括りである可能性が高い

## サブニッチ×10評価表

| サブニッチ | Momentum | Sticker Fit | Coloring Fit | Confidence | IP Risk | Competition | Trend Stage | 判定 |
|---|---|---|---|---|---|---|---|---|
| Bookish | N/A(成熟) | 85 | 40 | Medium | LOW | 高 | 4 | WATCH |
| Book Club | 高(F1-F4根拠) | 90 | 35 | Medium | LOW(固有ブランド名注意) | 中 | 3 | **BUILD_NOW** |
| Poetry | N/A | 70 | 45 | Low | MEDIUM(詩句直接引用注意) | 中 | 2〜3 | WATCH |
| Poetcore | N/A(仮説段階) | 75 | 55 | Low | LOW〜MEDIUM("Tortured Poets"類似表現注意) | 低 | 1 | TEST |
| Library | N/A | 70 | 65 | Low | LOW | 中 | 2〜3 | WATCH |
| Reading Journal | N/A | 88 | 30 | Medium | LOW | 中 | 3 | TEST |
| Books & Coffee | N/A(飽和) | 80 | 50 | Medium | LOW | 高 | 4〜5 | AVOID |
| Literary Girl | N/A | 65 | 45 | Low | MEDIUM | 中 | 1 | WATCH |
| Dark Academia | N/A(社内既存) | 82 | 68 | Medium | LOW | 中〜高 | 3 | TEST |
| Book Club Night | N/A | 72 | 40 | Low | LOW | 低 | 1 | WATCH |

## 総括
- 最も裏付けが強いのはBook Club本体(F1〜F4の関連検索語が軒並み高成長)。Etsy/Amazon双方に出品も存在。
- Poetcoreは仮説段階。実際のステッカー市場での商品化はほぼ確認できず(競合が薄いという意味ではTEST価値あり)。
- 新規発見の重要事実: 「BookTok」自体がByteDance/TikTokの登録商標、「Silent Book Club」も登録商標。Book Club系のフレーズ意匠は個別チェックが必要。

## 取得できなかった情報
Google Trends実測値(EGRESS_BLOCKED)。Etsy各カテゴリの正確な出品数・価格帯。記事本文の直接取得(bookriot.com/wavy.com等)。TikTok/Instagramの実際のハッシュタグ再生数・投稿数。

## 参照URL一覧
https://www.wkrg.com/news/pinterests-summer-2025-trend-report-books-clubs-are-in/ ・ https://www.wavy.com/news/national/pinterests-summer-2025-trend-report-books-clubs-are-in/ ・ https://bookriot.com/pinterest-reveals-gen-zs-bookish-interests-this-summer/ ・ https://fashionunited.com/news/fashion/poetcore-opera-aesthetic-and-brooches-key-style-predictions-from-pinterest-for-2026/2025121069575 ・ https://sourcingjournal.com/denim/denim-trends/pinterest-predicts-80s-maximalism-lace-poetcore-circus-2026-1234792760/ ・ https://www.trademarkia.com/booktok-97980756 ・ https://trademarks.justia.com/973/96/booktok-97396081.html ・ https://silentbook.club/pages/about-us ・ https://www.etsy.com/market/book_club_stickers ・ https://www.etsy.com/market/bookish_stickers ・ https://www.etsy.com/market/reading_journal_stickers ・ https://www.etsy.com/market/library_stickers ・ https://www.etsy.com/market/books_and_coffee_stickers ・ https://www.etsy.com/market/dark_academia_stickers ・ https://www.etsy.com/market/poetcore?facet=handmade ・ https://www.amazon.com/Book-Club-Stickers/s?k=Book+Club+Stickers ・ https://www.accio.com/business/bookish-stickers-top-sellers
