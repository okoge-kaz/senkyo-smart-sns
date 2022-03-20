## Twitter API

- Document
  - https://developer.twitter.com/en/docs/tools-and-libraries


## 城戸 Research
## 結論
　可能なら[**Twitter API v2**](https://developer.twitter.com/en/docs/twitter-api)が良いが
[**Twitter Analytics**](https://analytics.twitter.com/about)でもほとんど似た情報を手に入れられる。
 
## 概説
 まず[Twitter API v2](https://developer.twitter.com/en/docs/twitter-api)にはグレードとして、**Essential**,**Elevated**,**Academic Research**があり、それぞれのグレードに応じてできることが異なる。

以下にそれぞれのグレードにおける重要な[違い](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api)を述べる。
- **Essential**
    

| 料金 | Standard v1.1 | Premium v1.1 | Enterprise | Access to full-archive Tweet counts|
| -------- | -------- | -------- | --- |  --|
| 無料     | アクセス不可     | アクセス不可     | アクセス不可 | 不可能 |

- **Elevated**

| 料金 | Standard v1.1 | Premium v1.1 | Enterprise | Access to full-archive Tweet counts|
| -------- | -------- | -------- | --- |  --|
| 無料     | アクセス可能     | アクセス可能     | アクセス可能 | 不可能 |
- **Academic**

| 料金 | Standard v1.1 | Premium v1.1 | Enterprise | Access to full-archive Tweet counts|
| -------- | -------- | -------- | --- |  --|
| 無料     | アクセス可能     | アクセス可能     | アクセス可能 | 可能 |


また、本プロジェクトにおいては、顧客に対しコンサルティング業務を行うという性質上、インプレッション、エンゲージメントなどの要素が不可欠であるが、これを可能にするには[**Enterprise (-Gnip2.0)**](https://developer.twitter.com/en/docs/twitter-api/enterprise) の [**Engagement API**](https://developer.twitter.com/en/docs/twitter-api/enterprise/engagement-api/overview)を利用する必要があり、Twitter API v2の**Elevated**以上のグレードを使えば良いことがわかる。

> impression: ツイートを見たアカウントの数です。プロモーション対象のコンテンツに対するインプレッションのみを集計し、通常のツイートのインプレッションは含まれません。
> 
> engagement: ツイートに対するアカウントの反応を数値化したものです。リツイート、返信、いいね、投票、ハッシュタグのクリックなど、ツイートに対するあらゆるクリックを指し、課金対象外の獲得クリックも含まれます。
[source](https://business.twitter.com/ja/help/overview/twitter-ads-glossary.html#:~:text=%E4%BB%98%E3%81%91%E3%82%89%E3%82%8C%E3%81%BE%E3%81%99%E3%80%82-,%E3%82%A8%E3%83%B3%E3%82%B2%E3%83%BC%E3%82%B8%E3%83%A1%E3%83%B3%E3%83%88%E6%95%B0,%E3%82%AF%E3%83%AA%E3%83%83%E3%82%AF%E3%82%82%E5%90%AB%E3%81%BE%E3%82%8C%E3%81%BE%E3%81%99%E3%80%82)

ただし、本プロジェクトにおいては**Academic**グレードにする必要があるかは疑問。理由として上表の[Access to full-archive Tweet counts](https://developer.twitter.com/en/docs/twitter-api/tweets/counts/introduction)は一例として
>フルアーカイブのツイート数エンドポイントを使用して、2017年8月から9月までの1日あたりのハッシュタグ#SOSHurricaneHarveyのツイート数を確認できます。

このように使われるものであり、今回のプロジェクトには必要でないと思われるからである。

(APIを利用することでどこまで自動化できるのかがよくわかっていないので判断出来かねるが）もしAPIを利用してもエンゲージメント等を纏めるのに手動でしないといけないことが多少でもあるならば、本プロジェクトにおいて必要な情報は、どのツイートにどの程度のインプレッション、エンゲージメント、いいね、RT、プロフィールに訪れた人がいたかどうかであると思っているので、[**Twitter Analytics**](https://analytics.twitter.com/about)を利用するのも手だと思われる。Export data(csv)というボタンがあるのですぐにcsvファイルに落とすことが可能。
- 以下私のツイッターアカウントのAnalytics
         ![](https://i.imgur.com/aAj6W8C.png)
このように、各ツイートのいいね数やprofile click数が一覧で表示される。(これは各ツイートごとにまとめられているが、一日あたりのツイート数、いいね数でまとめることもできる)
        　![](https://i.imgur.com/uy06Krc.jpg)
**※どのような人がRTしたのかの情報は手に入れられない(数字の情報しか得られない)のでそれらが必要な場合は不適切かもしれません。**

## 懸念事項

- 料金について
　Twitter API v2をElevated(無料)にした場合enterpriseの利用権もついてくるというような[表](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api)がありましたが、それまでenterpriseだけで有料だったものが本当に無料になるのかがわかりません。思いつく限りの検索ワードで調べてみたのですが目ぼしいものがなく困っています。
  >新しいTwitter APIでは、開発者が開発を簡単に始められたり、開発規模を拡大したりできるよう、複数のアクセスレベルを設けています。これまで、Twitter　APIはスタンダード（無料）、プレミアム（有料のセルフサービス型）、エンタープライズ（有料のカスタムAPI）という3つに分かれ、それぞれ異なるプラットフォームやエクスペリエンスを提供していました。開発者もニーズの変化や拡大に伴って、それぞれのAPIの行き来は面倒な作業になりました。今後は、研究者からメーカーや企業に至るまで、すべての開発者が同じAPI上を使用して高いレベルでのアクセスと拡張を実現できるようになります。
  >[source](https://blog.twitter.com/developer/ja_jp/topics/tools/2020/NewTwitterAPI)
 

## 藤井 Research

参考:

[Twitter Developer Platform](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api#v2-access-leve)

Elevated access levelにすることで、API を利用することができる。
料金は無料ではあるが、いくつか質問事項に答える必要がある。

また、Twitter API には [Tools and Libraries](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/v2)で紹介されているように、Python, Typescriptなどの言語を用いて、API を利用することができる。

特に、tweepyでは retweet の数や、 retweetしたユーザーの情報などを取得することができる。
[参考](https://docs.tweepy.org/en/stable/client.html#tweepy.Client.retweet)


