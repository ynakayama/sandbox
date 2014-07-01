#!/opt/ruby/current/bin/ruby
# -*- coding: utf-8 -*-

$:.unshift File.join(File.dirname(__FILE__))

class Reducer
  def self.reduce(stdin)
    key = newkey = ""

    stdin.each_line {|line|
      key, mac_str, rmac_str, rssi_val, humantime, time_diff = line.strip.split("\t")
      tar_file, timestamp = key.split(",")
      puts "#{tar_file}\t#{timestamp}\t#{mac_str}\t#{rmac_str}\t#{rssi_val}\t#{humantime}\t#{time_diff}\n"
    }
  end
end

if __FILE__ == $0
  Reducer.reduce($stdin)
end
