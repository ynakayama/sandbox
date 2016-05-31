require "net/http"
require "uri"
require "rexml/document"

host = "172.16.xxx.xxx"
api = "http://#{host}:8080/api"
uri = URI.parse(api)

response = nil

request = Net::HTTP::Post.new(uri.request_uri)
request.body = <<EOS
<?xml version="1.0" encoding="UTF-8"?>
<logst apiversion="1.1.0">
    <header/>
    <body>
        <login user="user" pass="pass"/>
    </body>
</logst>
EOS

http = Net::HTTP.new(uri.host, uri.port)

# http.use_ssl = true
# http.verify_mode = OpenSSL::SSL::VERIFY_NONE

http.set_debug_output $stderr

http.start do |h|
  response = h.request(request)
end

doc = REXML::Document.new(response.body)
doc.elements.each do |element|
  puts "レスポンス本文全体"
  puts element

  puts "エレメント個別"
  puts element.elements["header"].elements["status code"].text
  puts element.elements["body"].elements["jsessionid value"]
end
