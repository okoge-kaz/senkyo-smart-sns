## Facebook API に関する分析

- Document
  - https://developers.facebook.com/docs/graph-api?locale=ja_JP
  - https://developers.facebook.com/docs/marketing-apis/overview
## 結論(藤井)

~~[Ad Account Insights](https://developers.facebook.com/docs/graph-api/reference/adaccount/insights?locale=ja_JP)を用いるのが望ましい。~~

## 概説(藤井)

~~インサイト等の情報を取得する必要性があることを踏まえると、Insightsを取得できるAPIが上記のものしかない。~~
[詳細](https://developers.facebook.com/docs/marketing-api/insights?locale=ja_JP)


## はじめに(城戸)
以下概説においてPageという用語が出てくるが、(私が)知らなかったので解説を載せておきます
 #### プロフィール、ページの違い
  > プロフィール
> Facebookプロフィールは、趣味・関心、写真、動画、居住地、出身地など、自分に関する情報をシェアできる場所です。自分のプロフィールを見るには、Facebookの画面上部にある自分の名前またはプロフィール写真を クリックまたはタップします。
> 
> ページ
> ページを作成したり、管理したりするには、プロフィールが必要です。Facebookページは、アーティスト、著名人、ビジネス、ブランド、組織、非営利団体などがファンや顧客とつながることができる場所です。Facebookで  ページに「いいね！」したり、ページをフォローしたりすると、フィードにそのページの最新情報が表示されるようになります。

- ページの一例
　　![](https://i.imgur.com/FIT0QRu.png)

> Q : facebookページを作成するのと個人用facebookアカウントの公開コンテンツのフォローを許可するのはどっちがいいのでしょうか?
A : Facebookでビジネス、ブランド、または製品の存在を示すことを目的としている場合は、Facebookページを作成してください。Facebookページは多くの利用者と交流するのに適した機能で、エンゲージメントを管理および追跡するのに役立つツールもそろっています。
個人のタイムラインでより多くの人に最新情報を見てもらうことを目的としている場合は、フォローの許可をおすすめします。フォローを許可すると、Facebookで友達ではない人を含め、すべてのFacebookの利用者があなたをフォローし、自分のニュースフィードであなたの公開コンテンツを確認できるようになります。

[引用](https://www.facebook.com/help/135275340210354/?helpref=hc_fnav)

政治家がfacebookページを利用するべきか、しないべきかはわからないが、上からわかるように分析をするための情報を手に入れられるのはページだけだと思われる。

ページを利用している政治家の例 [小泉進次郎](https://www.facebook.com/shinjiro.koizumi)

ページを利用していない政治家の例 [安倍晋三](https://www.facebook.com/abeshinzo)

## 結論(城戸)

[**Graph API**](https://developers.facebook.com/docs/graph-api?locale=ja_JP)の[**Page Insights**](https://developers.facebook.com/docs/graph-api/reference/v13.0/insights)用いるのが望ましい。


## 概説(城戸)

### グラフAPIでできること(今回必要そうなもの)
#### [Page Insights](https://developers.facebook.com/docs/graph-api/reference/v13.0/insights)
 - [Page Post](https://developers.facebook.com/docs/graph-api/reference/v13.0/insights#:~:text=day%2C%20week%2C%20days_28-,Page%20Posts,-Metric%20Name)
    - あなたのページの投稿が利用者の画面に表示された回数
    - あなたのページの投稿が画面に表示された人の数
 - [Page Post Engagement](https://developers.facebook.com/docs/graph-api/reference/v13.0/insights#:~:text=day%2C%20week%2C%20days_28-,Page%20Post%20Engagement,-Metric%20Name)
    - あなたの投稿をクリックした人数
    - ページに「いいね！」して、投稿で何らかのアクションを実行した人
 - [Page Post Impression](https://developers.facebook.com/docs/graph-api/reference/v13.0/insights#:~:text=to%20an%20event-,Page%20Post%20Impressions,-Metric%20Name)
    - あなたのページの投稿が利用者の画面に表示された回数。投稿には、ステータス、写真、リンク、動画なども含まれます。
    - あなたのページの投稿が画面に表示された人の数。
    - あなたのページでの投稿を見て、ページに「いいね！」した人数
 - [Page Post Reactions](https://developers.facebook.com/docs/graph-api/reference/v13.0/insights#:~:text=lifetime-,Page%20Post%20Reactions,-The%20%22like%22%20reaction)
    - 投稿への「いいね！」の合計数
    - 投稿への「超いいね！」の合計数　
 - [Page Engagement](https://developers.facebook.com/docs/graph-api/reference/v13.0/insights#:~:text=day%2C%20week%2C%20days_28-,Page%20Engagement,-The%20%22like%22%20reaction)
    - ページでアクションを実行した人の数
    - 投稿でリアクションやコメント、シェアなどのアクションが実行された回数
    - あなたのコンテンツのクリック数
    - あなたのコンテンツをクリックした人数
  - [Page Impression](https://developers.facebook.com/docs/graph-api/reference/v13.0/insights#:~:text=day-,Page%20Impressions,-Metric%20Name)
    - あなたのページのコンテンツ、またはあなたのページに関するコンテンツが利用者の画面に表示された回数
    - あなたのページのコンテンツ、またはあなたのページに関するコンテンツが画面に表示された人の数
  - [Page User Demographic](https://developers.facebook.com/docs/graph-api/reference/v13.0/insights#:~:text=day-,Page%20User%20Demographics,-Metric%20Name)
    - あなたのページに「いいね！」した人の市区町村別のFacebook位置情報

#### [URL](https://developers.facebook.com/docs/graph-api/reference/v13.0/url)　(今回のプロジェクトにおいてあまり関係ない可能性が高い)
  -  URLに付けられたコメントの数  
  -  URLに対するリアクションの数
  -  URLがシェアされた回数
  > URLNodeのAppLinksデータやエンゲージメント数などのフィールドを取得します。注: エンゲージメント数は意図的に不正確な値になっていますが、URLによるユーザーエンゲージメントを正確に反映していることは信頼できます。
  [引用](https://developers.facebook.com/docs/graph-api/reference/v13.0/url))

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


