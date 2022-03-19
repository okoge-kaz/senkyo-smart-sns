## Twitter API

- Document
  - https://developer.twitter.com/en/docs/tools-and-libraries


## 城戸 Research

- API 取得まで 
  - engagement,インプレッション等は法人プラン**enterprise API**の**Twitter Engagement API**を利用する(Premium APIs 等のプランでは不可能)。いいね数は enterprise API でなくても手に入れられる。[詳細](https://developer.twitter.com/en/docs/twitter-api/enterprise/engagement-api/overview) 
    - 料金 ⇨ 　([ここ](https://developer.twitter.com/en/products/twitter-api/enterprise/application)に情報を入力しないと)詳細不明　[How much pricing in enterprise plan engagement API?](https://twittercommunity.com/t/how-much-pricing-in-enterprise-plan-engagement-api/112738)
  料金の推測(それなりにすると思われる)

    [①](https://developer.twitter.com/en/pricing/search-30day) 
    > API のグレードとして、Standard,Premium,enterprise があり、料金もグレードが上がるにつれて高くなると考えられるが、過去 30 日のツイートを得られる API の Premium バージョンは 500Tweets/1Request、500Requests/1month で＄ 149.00 となりリクエストの上限の増加に対して比例的に増加する。

    [②](https://japan.cnet.com/article/35119321/#:~:text=%E7%84%A1%E6%96%99%E7%89%88%E3%81%A7%E3%81%AF%E6%89%B1%E3%81%88%E3%82%8B%E3%82%A2%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88,1%E6%9C%88%E3%81%82%E3%81%9F%E3%82%8A2899%E3%83%89%E3%83%AB%E3%80%82)

    > Account Activity APIでは、ツイートやリプライ、ダイレクトメッセージなどの通知などがリアルタイムで受信できる。タイムラインのデータを自動で取得する機能は盛り込まれていない。

  Account Activity API は、無料で提供するサンドボックス、有料提供となるプレミアム、エンタープライズの 3 段階が設定。無料版では扱えるアカウント数が 15 個に限られるほか、プレミアム版でも 25 個～ 250 個の制限が設けられており、251 個以上のアカウントを扱う場合は、エンタープライズ契約が必要となる。プレミアム版の価格は扱えるアカウント数によって異なり、25 個までが 1 月あたり 339 ドル、250 個までが 1 月あたり 2899 ドル。

- API を利用しない(できない)場合は[**Twitter Analytics**](https://analytics.twitter.com/about)を利用すると良いと思われる。Export data(csv)というボタンがあるのですぐに csv ファイルに落とすことが可能。 - 以下私のツイッターアカウントの Analytics - 月ごとの情報
  ![](https://i.imgur.com/9EVAOQL.jpg) - 各ツイートに対するエンゲージ
  ![](https://i.imgur.com/iBbmnid.jpg) - 出力した csv ファイル(By Tweet)
  ![](https://i.imgur.com/aAj6W8C.png)


## 藤井 Research

参考:

[Twitter Developer Platform](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api#v2-access-leve)

Elevated access levelにすることで、API を利用することができる。
料金は無料ではあるが、いくつか質問事項に答える必要がある。

また、Twitter API には [Tools and Libraries](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/v2)で紹介されているように、Python, Typescriptなどの言語を用いて、API を利用することができる。

特に、tweepyでは retweet の数や、 retweetしたユーザーの情報などを取得することができる。
[参考](https://docs.tweepy.org/en/stable/client.html#tweepy.Client.retweet)


