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
- [分類項目](https://developers.google.com/youtube/reporting/v1/reports/dimensions)
    - 動画ごと
    - プレイリストごと
    - チャンネルごと
    - アセット
    - 国
    - 米国の州・準州
    - **日付**
    - 再生場所
      - Youtubeアプリから
      - Webサイト上の埋め込み動画から
        - Webサイト上の埋め込み動画のみ、どのURLでの再生かで分類できる
      - その他
    - ライブ中の情報かオンデマンドでの情報か
    - 視聴者がチャンネル登録者かどうか
    - どこからこの動画に飛んできたか
      - 直接
      - YoutubeのCMから
      - Youtubeのカテゴリ機能から
      - チャンネルから
      - Youtubeの検索機能から
      - 関連動画から
      - その他
      - googleでの検索から
      - アノテーションから
        - アノテーションとは動画中に画面に表示できるリンクのことです。
      - 再生リスト再生中に本動画に流れてきた
      - 通知から
      - 再生リスト一覧ページから本動画に飛んできた
      - エンドスクリーンから
        - Youtubeでの動画のエンドロール時に表示させることができる「おすすめ動画」などのリンクのことです。
      - ストーリーから
        - ストーリーとは一定期間で自動削除される短めの動画です。
      - ショートから
        - ショートとは自動削除されない短めの動画です。
      - 商品紹介ページから
      - ハッシュタグから
      - ライブリダイレクトから
        - プレミア公開の前にライブ配信を行うとライブ配信終了後に視聴者を自動でプレミア公開に誘導できる仕組み[参考](https://support.google.com/youtube/answer/10359590?hl=ja)
    - 閲覧デバイスの種類
      - 不明
      - パソコン
      - テレビ
      - ゲーム機
      - 携帯電話
      - タブレット
    - デバイスのOSの種類
    - 年齢
      - 13~17
      - 18~24
      - 25~34
      - 35~44
      - 45~54
      - 55~64
      - 64~
    - 性別
    - どのサービスでコンテンツを共有されたか[参考](https://developers.google.com/youtube/reporting/v1/reports/dimensions?hl=ja#Social_Dimensions)
      - Yahoo!Japan
      - Google など
    - アノテーションのタイプ
      - 吹き出し
      - タイトル　など
    - どのアノテーションから飛んできたか
    - カードのタイプ
    - どのカードから飛んできたか
    - エンドスクリーンのタイプ
    - どのエンドスクリーンから飛んできたか
    - 字幕の言語
    - 動画再生中に再生された広告の種類

  - [取得情報の項目](https://developers.google.com/youtube/reporting/v1/reports/metrics)
    - 視聴回数
    - Youtube Premiumのメンバーが動画を視聴した回数
      - Youtube PremiumとはYoutubeの有料サブスク機能
    - 視聴中にアカウントにログインした視聴者の割合
    - 総再生時間関連
      - 視聴分数
      - Youtube Premiumのメンバーが動画を視聴した分数
      - ビデオ再生の平均時間(秒)
    - エンゲージメント関連
      - ユーザーが動画にコメントした回数
      - 高評価数
      - 低評価数
      - 共有ボタンにて共有をおこなった回数
      - チャンネル登録数
      - チャンネル退会数
    - 再生リスト関連
      - 再生リスト追加数
      - 再生リストから削除された数
      - 視聴者が再生リストの再生を開始した回数
      - 視聴者がプレイリストに保存した回数
      - 視聴者がプレイリストから削除した回数
    - アノテーション関連
      - クリックできるアノテーションの表示回数
      - 視聴者のアノテーションのクリック回数
      - アノテーションの総数に対する視聴者がクリックしたアノテーションの比率
      - 閉じれるアノテーションの表示回数
      - 視聴者がアノテーションを閉じた回数
      - アノテーションの総数に対する視聴者が閉じたアノテーションの比率
    - カード関係
      - カード表示回数
        - カードとは動画中に出すことができるリンクのこと
      - 視聴者がカードをクリックした回数
      - カード表示回数に対するカードのクリック率
      - カードのティザー(説明文)が表示された回数
      - 視聴者がカードのティザーをクリックした回数
      - カードのティザー表示回数に対するカードのクリック率
    - エンドスクリーン関係
      - エンドスクリーンの表示回数
      - 視聴者がエンドスクリーンの要素をクリックした回数
      - エンドスクリーンの表示回数に対する視聴者のエンドスクリーンのクリック回数の比率
    - 視聴者保持率
      - 動画の特定の時点で動画を視聴している視聴者の絶対比率
    - 広告収益関連
      - 選択した範囲、地域での広告、非広告から得た推定純利益の合計
      - 選択した範囲、地域での広告から得た推定純利益の合計
      - AdSenseでの広告からの推定利益の合計
        - AdSenseとは広告を自動で貼ってくれるシステム
      - DoubleClickやその他から得た推定純利益の合計
      - Youtube Premiumによる推定利益
      - 有料コンテンツやファンからのファウンディングによる利益からパートナー料金を差し引いた利益
    - 広告関連
      - 選択した範囲、地域での広告総収入
      - 広告1000回あたりの予想利益
      - 1000回の再生あたりの推定総収入
- 料金
  - 無料で利用可能
  - アクセス制限の上限を上げたい場合には申請が必要だがその際に追加料金がかかるかは不明



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
