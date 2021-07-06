#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import MeCab
mecab = MeCab.Tagger("-Ochasen")
m = mecab.parseToNode("昨日、急に思い立ってザリガニを飼ってみた。")
cnt = 0
while m:
    print(m.surface, "\t", m.feature)
    if m.surface.find('BOS/EOS') >= 0 or len(m.surface) == 0:
        m = m.__next__
        continue
    feat = m.feature
    arr = feat.split(',')
    gram = arr[0]  # 品詞
    word = arr[6]  # 原形
    if gram in ('名詞', '動詞', '形容詞'):
        print(gram, word)

    cnt = cnt + 1
    m = m.__next__
