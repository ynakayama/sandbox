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
      "20140312.tar.gz\tBBCCDDEE1122\tShop15\t14\t1394559961\t2014-03-12 02:46:01 +0900\t-1\n" +
      "20140312.tar.gz\tCCDDEEAA2233\tShop10\t33\t1394560109\t2014-03-12 02:48:29 +0900\t60\n" +
      "20140312.tar.gz\tCCDDEEAA2233\tShop11,Shop12,Shop13\t18,11,28\t1394560046\t2014-03-12 02:47:26 +0900\t100\n" +
      "20140312.tar.gz\tCCDDEEAA2233\tShop14\t26\t1394559946\t2014-03-12 02:45:46 +0900\t-1\n"
    }

    it 'Mapper の出力のうち一定間隔以内のレコードについてはまとめて出力される' do
      expect(subject).to eq expected
    end
  end
end
