## Facebook API に関する分析

- Document
  - https://developers.facebook.com/docs/graph-api?locale=ja_JP
  - https://developers.facebook.com/docs/marketing-apis/overview
## 結論(藤井さん)

~~[Ad Account Insights](https://developers.facebook.com/docs/graph-api/reference/adaccount/insights?locale=ja_JP)を用いるのが望ましい。~~\

## 概説(藤井さん)

インサイト等の情報を取得する必要性があることを踏まえると、Insightsを取得できるAPIが上記のものしかない。   
[詳細](https://developers.facebook.com/docs/marketing-api/insights?locale=ja_JP)

##結論(城戸)

[Graph API](https://developers.facebook.com/docs/graph-api?locale=ja_JP)を用いるのが望ましい。

##　概説(城戸)

### [グラフAPIでできること](https://developers.facebook.com/docs/graph-api/reference/v13.0/url)(必要なさそうなものは線)
 - URLにつけられたコメント数の取得
 - URLにつけられたリアクション(主にいいね)の数の取得
 - URLがシェアされた回数
 - ~~あなたのサイトで[Comments Plugin](https://developers.facebook.com/docs/plugins/comments/)を使用して集めたプラグインのコメント数の取得~~　

### [Page Insights](https://developers.facebook.com/docs/graph-api/reference/v13.0/insights)


API以外の方法

 - [**Creator Studio**](https://business.facebook.com/creatorstudio/home)を使う。

## 懸念事項

Ad Account Insightsが対応しているのがあくまでも広告だけで、個人の投稿に対するインサイトを取得することができない可能性がある。

↑おそらく不可能だと思われる。広告アカウントは通常の個人のアカウントとは**別に**作らなければならないのでそれ専用の統計である可能性が高い。
  ![](https://i.imgur.com/oCb66uF.png)

[参考](https://liskul.com/facebook-ads-account-93916#:~:text=%E3%81%99%E3%82%8B%E3%82%A2%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88%E3%81%A8%E3%81%AF-,%E5%88%A5%E3%81%AB,-%E3%80%81%E5%BA%83%E5%91%8A%E3%82%92%E9%85%8D%E4%BF%A1)(公式ドキュメントにも同様の内容があったがどこに載っていたか忘れたのでとりあえず仮置きとして置いておきます。見つけたらリンク先を修正します。)

- 以下私のfacebookアカウントで広告をしようとした場合に表示されたもの
      ![](https://i.imgur.com/rMf6ldK.png)
      ![](https://i.imgur.com/REvahc2.png)
  上にわかるように通常のアカウントとは全く別に作る必要がある。
