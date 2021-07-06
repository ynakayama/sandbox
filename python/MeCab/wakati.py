#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import MeCab

wakati = MeCab.Tagger("-O wakati")
print(wakati.parse('最近の夜は寒い'))
