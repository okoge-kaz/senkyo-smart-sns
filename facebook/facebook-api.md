## Facebook API に関する分析

- Document
  - https://developers.facebook.com/docs/graph-api?locale=ja_JP
  - https://developers.facebook.com/docs/marketing-apis/overview
## 結論

[Ad Account Insights](https://developers.facebook.com/docs/graph-api/reference/adaccount/insights?locale=ja_JP)を用いるのが望ましい。

## 概説

インサイト等の情報を取得する必要性があることを踏まえると、Insightsを取得できるAPIが上記のものしかない。   
[詳細](https://developers.facebook.com/docs/marketing-api/insights?locale=ja_JP)

### [グラフAPIでできること](https://developers.facebook.com/docs/graph-api/reference/v13.0/url)(必要なさそうなものは線)
 - URLにつけられたコメント数の取得
 - URLにつけられたリアクション(主にいいね)の数の取得
 - URLがシェアされた回数
 - ~~あなたのサイトで[Comments Plugin](https://developers.facebook.com/docs/plugins/comments/)を使用して集めたプラグインのコメント数の取得~~　

API以外の方法

 - [**Creator Studio**](https://business.facebook.com/creatorstudio/home)を使う。

## 懸念事項

Ad Account Insightsが対応しているのがあくまでも広告だけで、個人の投稿に対するインサイトを取得することができない可能性がある。
