#!/opt/ruby/current/bin/ruby
# -*- coding: utf-8 -*-

$:.unshift File.join(File.dirname(__FILE__))

class Mapper
  def self.map(stdin)
    stdin.each_line {|line|
      tar_file, mac_str, rmac_str, rssi_val, timestamp, humantime, time_diff = line.strip.split("\t")
      diff = time_diff.to_i

      unless diff >= 0 and diff < 10
        puts "#{tar_file},#{timestamp}\t#{mac_str}\t#{rmac_str}\t#{rssi_val}\t#{humantime}\t#{time_diff}\n"
      end
    }
  end
end

if __FILE__ == $0
  Mapper.map($stdin)
end
