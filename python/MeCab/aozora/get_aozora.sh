#!/bin/sh

curl -L -o $HOME/tmp/2093_ruby_28087.zip http://www.aozora.gr.jp/cards/000096/files/2093_ruby_28087.zip
unzip -d $HOME/tmp ~/tmp/2093_ruby_28087.zip
rm ~/tmp/2093_ruby_28087.zip
ruby ~/scripts/aozora_prepare.rb ~/tmp/dogura_magura.txt ~/tmp/dogura_magura_utf8.txt
rm ~/tmp/dogura_magura.txt
python extract_noun.py ~/tmp/dogura_magura_utf8.txt
