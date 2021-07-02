#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from nose.tools import *
from extract_category_map import *

def test_start():
    f1 = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'test_filename.txt')
    f2 = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'test_exclude.txt')
    args = [__file__, f1, f2]
    analyzer = Analyzer(args)
    result = analyzer._read_from_exclude()
    eq_(['ABC', 'ABD'], result)
