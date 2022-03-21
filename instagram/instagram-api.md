## Instagram API

- Document  
  https://developers.facebook.com/docs/instagram

## 結論

[Instagram グラフ API](https://developers.facebook.com/docs/instagram-api)を使用することが望ましいので、Instagram Business または Instagram Creator へのアカウントの変更を必要とする。

> この API を使用して、メディアの取得と公開、メディアへのコメントの管理と返信、他の Instagram ユーザーが@mention したメディアの識別、ハッシュタグ付きのメディアの検索、他の Instagram Business および Instagram Creator に関する基本メタデータと指標の取得を行えます。

とあるように、データを収集するセンキョ側のアカウント及び、データを収集される政治家さん側のアカウントの両方が前述の Instagram Business または、Instagram Creator にアカウントを変更しておく必要がある。

## 概説

### 経緯

[Instagram 基本表示 API](https://developers.facebook.com/docs/instagram-basic-display-api?locale=ja_JP)では、

> Instagram 基本表示 API により、あなたのアプリのユーザーが各自の Instagram アカウントの基本的なプロフィール情報、写真、動画を取得することを許可できます。

> この API を利用してどのタイプの Instagram アカウントにもアクセスできますが、基本データに対する読み取りアクセス権しか提供されません。

とあるように、以下のような情報しか取得することができない。

1. Instagram ユーザーから Instagram ユーザーアクセストークンおよびアクセス許可を取得する
2. Instagram ユーザーのプロフィールを取得する
3. Instagram ユーザーの画像、動画、アルバムを取得する

しかしながら、本プロジェクトにおいては、顧客に対しコンサルティング業務を行うという性質上、インプレッション、エンゲージメントなどの要素が不可欠であるため、Instagram 基本表示 API では要件を満たせていない。

その点、Instagram グラフ API を使用すると IG ユーザー([注](#用語補足))とその[IG メディア](https://developers.facebook.com/micro_site/url/?click_from_context_menu=true&country=JP&destination=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Finstagram-api%2Freference%2Fig-media&event_type=click&last_nav_impression_id=058Mn6Ymb3NMpi2RF&max_percent_page_viewed=44&max_viewport_height_px=913&max_viewport_width_px=1680&orig_http_referrer=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Finstagram-api%2Fguides%2Finsights&orig_request_uri=https%3A%2F%2Fdevelopers.facebook.com%2Fajax%2Fdocs%2Fnav%2F%3Fpath1%3Dinstagram-api%26path2%3Dguides%26path3%3Dinsights&region=apac&scrolled=true&session_id=1GyuQxbx6CBYUg8uT&site=developers)オブジェクトのソーシャルインタラクション指標を取得できるため、Instagram グラフ API を使用することが望ましいと結論づけた。

### 用語補足

> IG ユーザー: Instagram ビジネスアカウントまたは Instagram クリエイターアカウントを指します。[source](https://developers.facebook.com/docs/instagram-api/reference/ig-user)

### API エンドポイント

[詳細](https://developers.facebook.com/docs/instagram-api/guides/insights#-------)

Instagram ビジネスアカウント、Instagram クリエイターアカウントの指標だけでなく、ユーザーの個別のメディアオブジェクトの指標を取得することが可能

## 制限

[Oficial Docs](https://developers.facebook.com/docs/instagram-api/guides/insights#--)

1. 一部の指標は、フォロワー数が 100 未満の IG ユーザーについては利用可能ではありません。
2. API は、オーガニックインタラクション指標のみを報告します。メディアオブジェクトを含んでいる広告で行われたインタラクションはカウントされません。
3. 指標データは 2 年間保存されます。
4. 一度に取得できるのは単一のユーザーのインサイトのみです。
5. Facebook ページのインサイトは取得できません。
6. ストーリーズがアーカイブまたはハイライトされていても、ストーリーズのインサイトを取得できるのは 24 時間のみです。有効期限が切れる前にストーリーズの最新のインサイトを取得するには、Instagram トピック用の Webhook を設定し、story_insights フィールドをサブスクリプション登録します。
7. アルバムの子 IG メディアのインサイトはサポートされていません。
8. リクエストしたインサイトデータが存在しない場合、または現在アクセスできない場合、API は個々の指標に対して 0 ではなく空のデータセットを返します。
