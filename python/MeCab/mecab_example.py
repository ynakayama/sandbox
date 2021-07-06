#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import MeCab
m = MeCab.Tagger("-Ochasen")
print(m.parse("太郎はこの本を二郎を見た女性に渡した。"))
