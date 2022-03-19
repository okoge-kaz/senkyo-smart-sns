## Youtube API

### Youtube Analytics API

### Youtube Data API

- Document
  - https://developers.google.com/youtube/v3/getting-started
- API 取得まで
  - Google アカウント取得
  - 本アプリ用の OAuth 設定(3~5 日要する)
  - Youtube Data API を有効化する
- 取得可能情報
  - https://developers.google.com/youtube/v3/guides/implementation?hl=en
  - **詳細は明日かく**
- 頻度制限
  - Google ではアクセスに伴うコストを Quotas で表す
  - デフォルトの上限は 10,000quatas/日(https://console.developers.google.com/iam-admin/quotas こちらから割り当て状況を確認可能)
    - A write operation that creates, updates, or deletes a resource：　 50units
    - A search request: 100units
    - 詳細：https://developers.google.com/youtube/v3/determine_quota_cost
