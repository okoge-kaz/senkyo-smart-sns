# Youtube APIに関する分析

## 結論
以下の順に好ましいと思われる。
  1. [YouTubeReportingAPI](https://developers.google.com/youtube/reporting/v1/reports?hl=ja)
  2. [YouTubeAnalyticsAPI](https://developers.google.com/youtube/analytics/data_model?hl=ja)
  3. [YouTubeDataAPI](https://developers.google.com/youtube/v3/getting-started?hl=ja)

## 概説
- YouTubeDataAPIは[実装リスト](https://developers.google.com/youtube/v3/guides/implementation?hl=ja)にある通り動画の投稿等の操作を実行するものであり顧客のコンサルティングに向いた機能を提供していない。

- 視聴者の情報を取得する機能を提供しているのはYouTubeAnalyticsAPIとYouTubeReportingAPIであり、双方ほとんど同じ機能を提供している。
- しかし、以下の点が異なる。


| 項目  | YouTubeAnalyticsAPI  |  YouTubeReportingAPI |
| ----  | ----  | ----  |
| データ範囲  | 1日, 1ヶ月  | 1日([30日前までのデータを利用可能](https://developers.google.com/youtube/reporting/v1/reports?hl=ja#historical-data)) |
| フィルタリング |  可能<br>特定の値を持つデータのみを取得可能　| 不可能<br>一括でダウンロード |
| アクセス制限 | クエリによって上限がある(注1) | データの編集がないため問題にならない |
| 片方のみで取得可能情報 | なし | <ul><li>字幕に関連するユーザーアクティビティ</li><li>プレイリストの視聴者維持率データ</li><li>コンテンツオーナー向け推定収益レポート</li></ul>|

- 注1 頻度制限について
  - Google ではアクセスに伴うコストを Quotas で表す
  - デフォルトの上限は 10,000quatas/日(https://console.developers.google.com/iam-admin/quotas こちらから割り当て状況を確認可能)
    - 書き込み、更新、削除：　 50quatas
    - 検索: 100quatas
    - 詳細：https://developers.google.com/youtube/v3/determine_quota_cost
  - 上限を上げる申請が可能
    - https://developers.google.com/analytics/devguides/config/mgmt/v3/limits-quotas?hl=ja

[source](https://developers.google.com/youtube/reporting#choose-the-right-api-for-your-application)

- 本プロジェクトでコンサルティングを行う際、1ヶ月以内の情報のみを使うのであれば問題なくYouTubeReportingAPIで問題なく情報を取得できる。
- 一方、それより前の情報を利用する場合は取得したデータを保管しておかないといけない。
- データがいつまで保管されているかについての言及はドキュメントの中に見つけられなかった。

### Youtube Analytics API
- Document
  - https://developers.google.com/youtube/reporting?hl=ja 
- 機能
  - 期間(7日、30日、1ヶ月間ごと)を指定してデータを取得可能
- 取得可能情報
  - [フィルタリング項目](https://developers.google.com/youtube/reporting/v1/reports/dimensions?hl=ja#adType)
    - 国
    - 動画
    - **期間(1日、1ヶ月)**
    - 視聴者がチャンネル登録者かどうか
    - どこからこの動画に飛んできたか
      - 検索から
      - 関連動画から
      - google検索の広告から
      - YoutubeのCMから　など
    - 閲覧デバイスの種類
    - 年齢
    - 性別
  - [取得情報の項目](https://developers.google.com/youtube/analytics/metrics)
    - 視聴回数
    - 視聴分数
    - 高評価集
    - チャンネル登録数
    - チャンネル退会数
    - 広告収益　など

- 注1 頻度制限について
  - Google ではアクセスに伴うコストを Quotas で表す
  - デフォルトの上限は 10,000quatas/日(https://console.developers.google.com/iam-admin/quotas こちらから割り当て状況を確認可能)
    - 書き込み、更新、削除：　 50quatas
    - 検索: 100quatas
    - 詳細：https://developers.google.com/youtube/v3/determine_quota_cost
  - 上限を上げる申請が可能
    - https://developers.google.com/analytics/devguides/config/mgmt/v3/limits-quotas?hl=ja
- 情報取得まで

### Youtube Reporting API
- Document
  - https://developers.google.com/youtube/reporting?hl=ja (同上)
- 機能
  - Youtube Analyticsを通して得た情報をまとめる
- 取得可能情報
  - [フィルタリング項目](https://developers.google.com/youtube/reporting/v1/reports/dimensions)
    - 国
    - 動画
    - **日付**
    - 視聴者がチャンネル登録者かどうか
    - どこからこの動画に飛んできたか
      - 検索から
      - 関連動画から
      - google検索の広告から
      - YoutubeのCMから　など
    - 閲覧デバイスの種類
    - 年齢
    - 性別
  - [取得情報の項目](https://developers.google.com/youtube/reporting/v1/reports/metrics)
    - 視聴回数
    - 視聴分数
    - 高評価集
    - チャンネル登録数
    - チャンネル退会数
    - 広告収益　など


### Youtube Data API

- Document
  - https://developers.google.com/youtube/v3/getting-started
- 機能
  - https://developers.google.com/youtube/v3/getting-started?hl=ja
- API 取得まで
  - Google アカウント取得
  - 本アプリ用の OAuth 設定(3~5 日要する)
  - Youtube Data API を有効化する
- [取得可能情報](https://developers.google.com/youtube/v3/guides/implementation?hl=en)
  - 対象のチャンネルの動画評価、共有、お気に入りへの追加などの情報
  - プレイリストの作成
  - 指定した検索パラメータに一致する検索結果　など

## API以外のツール
### Youtube アナリティクス
- Document
  - https://support.google.com/youtube/answer/9002587?hl=ja
- 機能
  - YouTubeReportingAPIやYouTubeAnalyticsAPIで取得可能な情報と同じような情報をグラフ化してくれる機能
- 利用画面
  - ![](https://i.imgur.com/gCbFeQa.png)
  - ![](https://i.imgur.com/8gTOyVt.png)
