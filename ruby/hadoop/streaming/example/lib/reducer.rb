#!/opt/ruby/current/bin/ruby
# -*- coding: utf-8 -*-

class Reducer
  def self.reduce(stdin)
    # 変数の初期化
    count = 0
    key = newkey = ""

    # 各行を逐次処理していく
    stdin.each_line {|line|
      # 1 行ごとに列に分解
      newkey, num = line.strip.split("\t")
      # 主キーが変化していないか監視する
      unless key == newkey
        # 変化していればカウントしていた合計値を出力する
        puts "#{key}\t#{count}\n"
        key = newkey
        count = 0
        newkey = ""
      end
      # キーが変化するまでカウンタを加算
      count += num.to_i
    }

    # 最後の 1 行が出力される機会が無いので
    puts "#{key}\t#{count}\n" unless key == ""
  end
end

if __FILE__ == $0
  Reducer.reduce($stdin)
end
