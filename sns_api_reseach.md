# SNS API　下調べ
## Twitter API
- Document
    - https://developer.twitter.com/en/docs/tools-and-libraries
- API取得まで
    - engagement,インプレッション等は法人プラン**enterprise API**の**Twitter Engagement API**を利用する(Premium APIs等のプランでは不可能)。いいね数はenterprise APIでなくても手に入れられる。[詳細](https://developer.twitter.com/en/docs/twitter-api/enterprise/engagement-api/overview)
        - 料金 ⇨　([ここ](https://developer.twitter.com/en/products/twitter-api/enterprise/application)に情報を入力しないと)詳細不明　[How much pricing in enterprise plan engagement API?](https://twittercommunity.com/t/how-much-pricing-in-enterprise-plan-engagement-api/112738)
            料金の推測(それなりにすると思われる)
            [①](https://developer.twitter.com/en/pricing/search-30day)
            >APIのグレードとして、Standard,Premium,enterpriseがあり、料金もグレードが上がるにつれて高くなると考えられるが、過去30日のツイートを得られるAPIのPremiumバージョンは500Tweets/1Request、500Requests/1monthで＄149.00となりリクエストの上限の増加に対して比例的に増加する。
            
            [②](https://japan.cnet.com/article/35119321/#:~:text=%E7%84%A1%E6%96%99%E7%89%88%E3%81%A7%E3%81%AF%E6%89%B1%E3%81%88%E3%82%8B%E3%82%A2%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88,1%E6%9C%88%E3%81%82%E3%81%9F%E3%82%8A2899%E3%83%89%E3%83%AB%E3%80%82)
            >　 Account Activity APIでは、ツイートやリプライ、ダイレクトメッセージなどの通知などがリアルタイムで受信できる。タイムラインのデータを自動で取得する機能は盛り込まれていない。
　Account Activity APIは、無料で提供するサンドボックス、有料提供となるプレミアム、エンタープライズの3段階が設定。無料版では扱えるアカウント数が15個に限られるほか、プレミアム版でも25個～250個の制限が設けられており、251個以上のアカウントを扱う場合は、エンタープライズ契約が必要となる。プレミアム版の価格は扱えるアカウント数によって異なり、25個までが1月あたり339ドル、250個までが1月あたり2899ドル。
 
-    APIを利用しない(できない)場合は[**Twitter Analytics**](https://analytics.twitter.com/about)を利用すると良いと思われる。Export data(csv)というボタンがあるのですぐにcsvファイルに落とすことが可能。
        -    以下私のツイッターアカウントのAnalytics
                - 月ごとの情報
        ![](https://i.imgur.com/9EVAOQL.jpg)
                - 各ツイートに対するエンゲージ
 ![](https://i.imgur.com/iBbmnid.jpg)
                - 出力したcsvファイル(By Tweet)
 ![](https://i.imgur.com/aAj6W8C.png)

 
 


            
## Instagram API
- Document
    - https://developers.facebook.com/docs/instagram
## Youtube API
### Youtube Analytics API

### Youtube Data API
- Document
    - https://developers.google.com/youtube/v3/getting-started
- API取得まで
    - Googleアカウント取得
    - 本アプリ用のOAuth設定(3~5日要する)
    - Youtube Data APIを有効化する
- 取得可能情報
    - https://developers.google.com/youtube/v3/guides/implementation?hl=en
    - **詳細は明日かく**
- 頻度制限
    - Googleではアクセスに伴うコストをQuotasで表す
    - デフォルトの上限は10,000quatas/日(https://console.developers.google.com/iam-admin/quotas こちらから割り当て状況を確認可能)
        - A write operation that creates, updates, or deletes a resource：　50units
        - A search request: 100units
        - 詳細：https://developers.google.com/youtube/v3/determine_quota_cost
## Facebook API
- Document
    - https://developers.facebook.com/docs/graph-api?locale=ja_JP

