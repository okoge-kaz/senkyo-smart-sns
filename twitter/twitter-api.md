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
- Engagement APIのエンドポイント [それぞれのメトリックの説明](https://developer.twitter.com/en/docs/twitter-api/enterprise/engagement-api/overview#:~:text=Tweets%20per%20request-,Available%20metrics,-The%20table%20below)
  - Current Totals: /totals
    - インプレッションの合計メトリックと、目的のツイートのエンゲージメントの合計メトリックを返す
    - インプレッション、エンゲージメント、お気に入り、返信、リツイート、引用ツイート、動画再生に限定される
    - OAuth 1.0aユーザーコンテキストを使用して、**過去90日以内に作成されたツイート**のインプレッションとエンゲージメントの指標を取得する機能をサポートします
    - OAuth 2.0 Bearerトークンを使用して、ツイートのお気に入り、リツイート、引用ツイート、返信、 および ビデオビューの メトリックを取得する機能をサポートします
    - 結果は、リクエストが行われた時点での現在のインプレッションとエンゲージメントの合計に基づいています
    - ダッシュボードレポートを強化し、さまざまな@handles全体のエンゲージメント率を計算するのに理想的です
    - リクエストごとに最大250ツイートのメトリックのリクエストをサポートします
  
  - Last 28 hours: /28hr
    - リクエストは、インプレッションの合計指標、エンゲージメントの合計指標、過去28時間に発生した個々のエンゲージメント指標の内訳を返すことができます
    - データは、ツイートIDごとにグループ化でき、時系列で集計、日ごと、または時間ごとにグループ化できます。
    - 最近作成されたコンテンツのパフォーマンスを追跡するのに理想的
    - 利用可能なすべてのメトリックをサポート
    - リクエストごとに最大25ツイートのメトリックのリクエストをサポートします

  - Historical: /historical
    - リクエストは、2014年9月1日以降の任意の期間（最長4週間）のインプレッション、エンゲージメント、および個々のエンゲージメント指標の内訳を返すことができます
    - リクエストは開始日と終了日のパラメータをサポートし、最大4週間の特定の時間枠に絞り込む柔軟性を提供します
    - データは、ツイートIDごとにグループ化でき、時系列で集計、日ごと、または時間ごとにグループ化できます。
    - 過去のベンチマークに対して最近のパフォーマンスを評価したり、@handleのパフォーマンスの過去の画像を作成したりするのに理想的です
    - 利用可能なすべてのメトリックをサポート
    - リクエストごとに最大25ツイートのメトリックのリクエストをサポートします
    
### 別の手法
(APIを利用することでどこまで自動化できるのかがよくわかっていないので判断出来かねるが）もしAPIを利用してもエンゲージメント等を纏めるのに手動でしないといけないことが多少でもあるならば、本プロジェクトにおいて必要な情報は、どのツイートにどの程度のインプレッション、エンゲージメント、いいね、RT、プロフィールに訪れた人がいたかどうかであると思っているので、[**Twitter Analytics**](https://analytics.twitter.com/about)を利用するのも手だと思われる。Export data(csv)というボタンがあるのですぐにcsvファイルに落とすことが可能。
- 以下私のツイッターアカウントのAnalytics
         ![](https://i.imgur.com/aAj6W8C.png)
このように、各ツイートのいいね数やprofile click数が一覧で表示される。
また、以下のように一日ごとにまとめることもできる。
        　![](https://i.imgur.com/uy06Krc.jpg)
**※どのような人がRTしたのかの情報は手に入れられない(数字の情報しか得られない)のでそれらが必要な場合は不適切かもしれません。**

## 懸念事項

- 料金について
　Twitter API v2をElevated(無料)にした場合enterpriseの利用権もついてくるというような[表](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api)がありましたが、それまでenterpriseだけで有料だったものが本当に無料になるのかがわかりません。
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


