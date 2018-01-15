require "mail"

mail = Mail.new do
  from     "ya-nakayama@dts.co.jp"
  to       "ya-nakayama@dts.co.jp"
  subject  "Windows からのメール送信テストです (Ruby)"
  body     File.read("body.txt", encoding: 'UTF-8:Shift-JIS')
  add_file "./attach.txt"
end

mail["Comments"] = "Some comments"

mail.smtp_envelope_from = "ya-nakayama@dts.co.jp"
mail.smtp_envelope_to   = "ya-nakayama@dts.co.jp"

mail.delivery_method(:smtp,
  address:        "mail.securemx.jp",
  port:           25,
  domain:         "dts.co.jp",
  authentication: nil,
  user_name:      nil,
  password:       nil
)

mail.deliver
