#!/opt/ruby/current/bin/ruby
# -*- coding: utf-8 -*-

$:.unshift File.join(File.dirname(__FILE__))

class Reducer
  def self.reduce(stdin)
    key = newkey = ""
    rmacs = []
    rvals = []

    stdin.each_line {|line|
      tar_file, mac_str, rmac_str, rssi_val, timestamp, humantime, time_diff, merge_flag = line.strip.split("\t")

      if merge_flag == "+"
        rmacs.push(rmac_str)
        rvals.push(rssi_val)
      else
        rmacs.push(rmac_str)
        rvals.push(rssi_val)
        puts "#{tar_file}\t#{mac_str}\t#{rmacs.join(',')}\t#{rvals.join(',')}\t#{timestamp}\t#{humantime}\t#{time_diff}\n"
        rmacs = []
        rvals = []
      end
    }
  end
end

if __FILE__ == $0
  Reducer.reduce($stdin)
end
