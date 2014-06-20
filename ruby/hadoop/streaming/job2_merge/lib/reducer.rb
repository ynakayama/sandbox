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

      rmacs.push(rmac_str)
      rvals.push(rssi_val)
      unless merge_flag == "+"
        puts "#{tar_file}\t#{mac_str}\t#{rmacs.join(',')}\t#{rvals.join(',')}\t#{timestamp}\t#{humantime}\t#{time_diff}\n"
        rmacs = []
        rvals = []
      end
    }
    if rmacs.length > 0
      puts "#{tar_file}\t#{mac_str}\t#{rmacs.join(',')}\t#{rvals.join(',')}\t#{timestamp}\t#{humantime}\t#{time_diff}\n"
    end
  end
end

if __FILE__ == $0
  Reducer.reduce($stdin)
end
