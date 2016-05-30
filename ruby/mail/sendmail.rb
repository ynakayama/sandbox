require "mail"

mail = Mail.new do
  from     "ya-nakayama@dts.co.jp" # 送信者メールアドレス
  to       "ya-nakayama@dts.co.jp" # 受信者メールアドレス
  subject  "subject text"          # タイトル
  body     File.read("body.txt")   # 本文
  add_file "./attach.txt"          # 添付ファイル
end

mail["Comments"] = "Some comments" # メールヘッダに任意の項目を追加

mail.smtp_envelope_from = "ya-nakayama@dts.co.jp" # エンベロープの送信者
mail.smtp_envelope_to   = "ya-nakayama@dts.co.jp" # エンベロープの受信者

mail.delivery_method(:smtp,
  address:        "mail.securemx.jp" # メールサーバーを指定
  port:           25,                # ポート番号を指定
  domain:         "dts.co.jp",       # ドメイン名を指定
  authentication: nil,               # 必要に応じて SMTP 認証を追加
  user_name:      nil,
  password:       nil
)

mail.deliver
