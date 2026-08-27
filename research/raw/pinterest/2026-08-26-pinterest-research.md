# Pinterest塗り絵トレンドリサーチ — 2026-08-26

調査エージェント: Pinterest塗り絵トレンドリサーチ
詳細版アーティファクト(37件の出典・成長率データ表つき): https://claude.ai/code/artifact/08094876-8019-4b02-9110-4696cf00a6e3

## 重大な制約
このセッションではWebFetchツールがネットワークegressポリシーにより完全にブロックされていました(pinterest.com、newsroom.pinterest.com、axios.com、nbcnews.com、en.wikipedia.orgまで全ドメインで`EGRESS_BLOCKED`)。セッション全体のネットワーク制約であり、特定サイトの問題ではない。そのため本調査はすべてWebSearchツールが返す検索結果スニペットのみに基づいており、記事本文の通読はできていない。

## 主な発見(公式Pinterestレポート由来、確認済み)
- **Pinterest Predicts 2026**(21トレンド):「nonconformity, self-preservation, escapism」が基調。Gen Zが67%を牽引
- **Spring Trend Report 2026**: garden inspiration ideas +940%、dark cottagecore kitchen +915%、**grandma core kitchen +545%**、comfy reading chair(small spaces) +455%
- **Hobbies Trend Report 2026**: **Kitchen Witch**トレンド(herbal apothecary +595%)、映画「Practical Magic 2」(2026年9月公開)とのタイアップで明確な季節性あり
- **Pinterest Palette**: 2025年は淡いコージー系(Butter Yellow/Cherry Red)、2026年はCool Blue/Jade/Plum Noir等「大胆で表現的」な方向へシフトと公式発表

## 個別テーマ候補の手がかり強度
- **強い公式シグナルあり**: grandma core aesthetic(+545%明記)、cozy witch aesthetic(Kitchen Witchと重なる、+595%系の数値あり)
- **二次情報のみ**: mushroom cottagecore(fantasy mushroom art +170%等、一次ソース未確認)
- **存在確認のみ(公式レポート言及なし)**: capybara aesthetic、cottagecore cats、cozy bakery aesthetic、bookstore aesthetic illustration — いずれもPinterestの「アイデアページ」が多数存在し検索カテゴリとして定着していることは確認できたが、成長率データは見つからず

## 季節性
Pinterestは年次(12月)に加え春・夏・秋(Hobbies)の季節別レポートを発行しており明確な季節連動あり。塗り絵出版系の二次情報では、祝日限定テーマは年間6〜8週間しか売れずエバーグリーンテーマの方がROIが高いとの指摘(Pinterest公式ではなく出版マーケ系メディアの見解)。

## 取得できなかった情報とその理由
- Pinterest検索結果ページ・個別ピンの保存数などの実データ(WebFetchが`EGRESS_BLOCKED`のため未取得)
- newsroom.pinterest.com等の一次レポート本文全文(WebSearch要約のみ)
- 塗り絵という単一カテゴリに絞った公式データ(多くはインテリア・ライフスタイル全般のトレンド)

詳細な出典一覧・成長率データ表・テーマ候補ごとのシグナル強度評価は上記アーティファクトを参照。
