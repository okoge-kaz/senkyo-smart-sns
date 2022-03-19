# Youtube Analytics API テスト用ファイル
## 環境構築
- これに従ってます
    - https://blog.codecamp.jp/youtube-analytics-python
- [Google APIコンソール](https://console.developers.google.com/?hl=JA)でプロジェクトを作成
- Google APIコンソールからYouTube Analytics APIを有効化
- 上記コンソール内のAPI設定画面からOAuth認証の設定を行い、OAuth client IDを作成、jsonファイルをダウンロードし作業ディレクトリへ(client_secret_444751859424-pj3t1mkmguhlbg8a4p3s64kncjs04dia.apps.googleusercontent.com.jsonは伊藤の認証ファイルです)
- 必要ライブラリのインストール
    - !pip install --upgrade google-api-python-client
    - !pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2
- [公式ドキュメント内](https://developers.google.com/youtube/analytics/reference/reports/query#examples_1)のyt_analytics_v2.pyをコピペ
    - 14行目の CLIENT_SECRETS_FILE = '〇〇' の部分を トークンファイル名に書き換え
    - 38行目の文末に,を足す
- yt_analytics_v2.pyを実行
- 表示されたリンクから認証を行う
- 請求した情報が表示