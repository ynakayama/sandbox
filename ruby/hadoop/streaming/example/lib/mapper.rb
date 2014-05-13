#!/opt/ruby/current/bin/ruby
# -*- coding: utf-8 -*-

require 'json'

class Mapper
  def self.map(stdin) # 標準入力が渡ってくる
    event_type = mac_str = ""

    # 各行を逐次処理していく
    stdin.each_line {|line|
      json = line.force_encoding("utf-8").strip
      # JSON パーサーで分解する
      JSON.parse(json).each {|k,v|
        # Mac アドレスを取り出す
        mac_str = v if k == "mac_str"
      }
      # 1 件カウントする
      puts "#{mac_str}\t1\n" unless mac_str == ""
      mac_str = ""
    }
  end
end

if __FILE__ == $0
  Mapper.map($stdin)
end
