#!/opt/ruby/current/bin/ruby
# -*- coding: utf-8 -*-

require 'json'

$:.unshift File.join(File.dirname(__FILE__))

class Mapper
  def self.map(stdin)
    event_type = mac_str = tar_file = timestamp = rmac_str = rssi_val = ""

    stdin.each_line {|line|
      json = line.force_encoding("utf-8").strip

      JSON.parse(json).each {|k,v|
        case k
        when "event_type"
          event_type = v
        when "mac_str"
          mac_str = v
        when "tar_file"
          tar_file = v
        when "timestamp"
          timestamp = format("%010d", v)
        when "rmac_str"
          rmac_str = v
        when "rssi_val"
          rssi_val = v
        end
      }

      if event_type == "rssi"
        puts "#{tar_file},#{mac_str},#{timestamp}\t#{rmac_str}\t#{rssi_val}\n" unless mac_str == ""
      end

      event_type = mac_str = tar_file = timestamp = rmac_str = rssi_val = ""
    }
  end
end

if __FILE__ == $0
  Mapper.map($stdin)
end
