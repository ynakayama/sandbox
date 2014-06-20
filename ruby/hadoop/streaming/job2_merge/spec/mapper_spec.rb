#!/usr/bin/env ruby
# -*- coding: utf-8 -*-

require 'rubygems'
require 'rspec'

class Mapper
  def self.run
    `cat test_data.txt | ruby lib/mapper.rb`
  end
end

describe Mapper do
  context '#run' do
    subject {
      Mapper.run
    }

    let(:expected) {
      "20140312.tar.gz\tBBCCDDEE1122\tShop15\t14\t1394559961\t2014-03-12 02:46:01 +0900\t-1\t-\n" +
      "20140312.tar.gz\tCCDDEEAA2233\tShop14\t26\t1394559946\t2014-03-12 02:45:46 +0900\t-1\t-\n" +
      "20140312.tar.gz\tCCDDEEAA2233\tShop13\t28\t1394560046\t2014-03-12 02:47:26 +0900\t100\t-\n" +
      "20140312.tar.gz\tCCDDEEAA2233\tShop12\t11\t1394560047\t2014-03-12 02:47:27 +0900\t1\t+\n" +
      "20140312.tar.gz\tCCDDEEAA2233\tShop11\t18\t1394560049\t2014-03-12 02:47:29 +0900\t2\t+\n" +
      "20140312.tar.gz\tCCDDEEAA2233\tShop10\t33\t1394560109\t2014-03-12 02:48:29 +0900\t60\t-\n"
    }

    it '一定時間間隔以内の同一キーの場合は + を付与、そうでない場合は - を付与する' do
      expect(subject).to eq expected
    end
  end
end
