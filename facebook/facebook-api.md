## Facebook API に関する分析

- Document
  - https://developers.facebook.com/docs/graph-api?locale=ja_JP
  - https://developers.facebook.com/docs/marketing-apis/overview
## 結論(藤井)

~~[Ad Account Insights](https://developers.facebook.com/docs/graph-api/reference/adaccount/insights?locale=ja_JP)を用いるのが望ましい。~~

## 概説(藤井)

~~インサイト等の情報を取得する必要性があることを踏まえると、Insightsを取得できるAPIが上記のものしかない。~~
[詳細](https://developers.facebook.com/docs/marketing-api/insights?locale=ja_JP)

## 結論(城戸)

[**Graph API**](https://developers.facebook.com/docs/graph-api?locale=ja_JP)の[**Page Insights**](https://developers.facebook.com/docs/graph-api/reference/v13.0/insights)用いるのが望ましい。

## 概説(城戸)

### グラフAPIでできること(今回必要そうなもの)
#### [Page Insights](https://developers.facebook.com/docs/graph-api/reference/v13.0/insights) 
 - [Page Engagement](https://developers.facebook.com/docs/graph-api/reference/v13.0/insights#:~:text=day%2C%20week%2C%20days_28-,Page%20Engagement,-The%20%22like%22%20reaction)
  
  - ページでアクションを実行した人の数
  - 投稿でリアクションやコメント、シェアなどのアクションが実行された回数
  - あなたのコンテンツのクリック数
  - あなたのコンテンツをクリックした人数
 [等](https://developers.facebook.com/docs/graph-api/reference/v13.0/insights#:~:text=day%2C%20week%2C%20days_28-,Page%20Engagement,-The%20%22like%22%20reaction)

### API以外の方法

 - [**Creator Studio**](https://business.facebook.com/creatorstudio/home)を使う。

#### Creator Studioでできること
 > 概要: リーチ、新規フォロワー、あなたのページのフォローをやめた人に関する指標を含め、すべてのページのパフォーマンスの概要を確認できます。下にスクロールすると、各ページのインサイトの概要が表示されます。インサイトには、動画の3秒再生数、動画の1分再生数、インプレッション、リーチした人数、エンゲージメントなどがあります。
 >
 > オーディエンス: 閲覧者とすべてのフォロワーについて、利用者層データの内訳を含めて詳しく見ることができます。オーディエンスインサイトについて、詳しくはこちらをご覧ください。

[引用](https://www.facebook.com/business/help/214952509306377?id=203539221057259)

## 懸念事項

Ad Account Insightsが対応しているのがあくまでも広告だけで、個人の投稿に対するインサイトを取得することができない可能性がある。

↑おそらく不可能だと思われる。広告アカウントは通常の個人のアカウントとは**別に**作らなければならないのでそれ専用の統計である可能性が高い。
  ![](https://i.imgur.com/oCb66uF.png)

[参考](https://liskul.com/facebook-ads-account-93916#:~:text=%E3%81%99%E3%82%8B%E3%82%A2%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88%E3%81%A8%E3%81%AF-,%E5%88%A5%E3%81%AB,-%E3%80%81%E5%BA%83%E5%91%8A%E3%82%92%E9%85%8D%E4%BF%A1)(公式ドキュメントにも同様の内容があったがどこに載っていたか忘れたのでとりあえず仮に置いておきます。見つけたらリンク先を修正します。)

- 以下私のfacebookアカウントで広告をしようとした場合に表示されたもの(一年程度前にアカウント作成済み)
      ![](https://i.imgur.com/rMf6ldK.png)
      ![](https://i.imgur.com/REvahc2.png)
  上にわかるように通常のアカウントとは全く別に作る必要がある。
