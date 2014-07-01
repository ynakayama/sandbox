#!/usr/bin/env ruby
# -*- coding: utf-8 -*-

require 'rubygems'
require 'rspec'

class Reducer
  def self.run
    `cat test_data.txt | ruby lib/mapper.rb | sort | ruby lib/reducer.rb`
  end
end

describe Reducer do
  context '#run' do
    subject {
      Reducer.run
    }

    let(:expected) {
      "20140312.tar.gz\t1394559946\tCCDDEEAA2233\tShop14\t26\t2014-03-12 02:45:46 +0900\t-1\n" +
      "20140312.tar.gz\t1394559946\tECDDEEAA2233\tShop14\t26\t2014-03-12 02:45:46 +0900\t-1\n" +
      "20140312.tar.gz\t1394559961\tBBCCDDEE1122\tShop15\t14\t2014-03-12 02:46:01 +0900\t-1\n" +
      "20140312.tar.gz\t1394559961\tDBCCDDEE1122\tShop15\t14\t2014-03-12 02:46:01 +0900\t-1\n" +
      "20140312.tar.gz\t1394560046\tCCDDEEAA2233\tShop13\t28\t2014-03-12 02:47:26 +0900\t100\n" +
      "20140312.tar.gz\t1394560046\tECDDEEAA2233\tShop13\t28\t2014-03-12 02:47:26 +0900\t100\n" +
      "20140312.tar.gz\t1394560109\tCCDDEEAA2233\tShop10\t33\t2014-03-12 02:48:29 +0900\t60\n" +
      "20140312.tar.gz\t1394560109\tECDDEEAA2234\tShop10\t33\t2014-03-12 02:48:29 +0900\t60\n"
    }

    it 'Mapper の出力をタイムスタンプ順にソートし整形した上で出力する' do
      expect(subject).to eq expected
    end
  end
end
