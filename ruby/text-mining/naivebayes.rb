# -*- coding: utf-8 -*-

require 'json'
require 'awesome_print'
require 'naivebayes'
require 'MeCab'

class NaiveBayesClassifier
  def initialize(args)
    @filename = args.shift || "json.txt"
    @classifier = NaiveBayes::Classifier.new(:model => "berounoulli")
    @mecab = MeCab::Tagger.new("-Ochasen")
  end

  def train
    @classifier.train("関心有り", {"北京" => 1, "香港" => 1, "中国" => 1})
    @classifier.train("関心無し", {"台風" => 1, "日本" => 1, "米国" => 1, "大阪" => 1, "京都" => 1, "神戸" => 1})
  end

  def classify
    classified = Array.new

    open(@filename) do |file|
      file.each_line do |line|
        key, tag, json = line.force_encoding("utf-8").strip.split("\t")
        hash = JSON.parse(json)
        hits = {}
        pickup_nouns(hash['title']).take(10).each {|word|
          if word.length > 1
            if word =~ /[一-龠]/
              hits.has_key?(word) ? hits[word] += 1 : hits[word] = 1
            end
          end
        }
        classify = @classifier.classify(hits)
        hash['classify'] = classify
        hash['key'] = key
        classified << hash
      end
    end

    classified
  end

  private

  def pickup_nouns(string)
    node = @mecab.parseToNode(string)
    nouns = []
    while node
      if /^名詞/ =~ node.feature.force_encoding("utf-8").split(/,/)[0] then
        nouns.push(node.surface.force_encoding("utf-8"))
      end
      node = node.next
    end
    nouns
  end
end

if __FILE__ == $0
  clf = NaiveBayesClassifier.new(ARGV)
  clf.train
  result = clf.classify
  ap result
end

