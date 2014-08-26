#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import pandas as pd

def list_files(path):
    dic = {}
    for root, dirs, files in os.walk(path):
        for filename in files:
            fullname = os.path.join(root, filename)
            if filename.startswith("hotnews") \
               and filename.endswith(".txt"):
                try:
                    print("Reading: %(filename)s" % locals())
                    df = pd.read_table(
                        os.path.join(path, filename), header=None)
                    dic[filename] = df
                except pd.parser.CParserError:
                    print("Skip: %(filename)s" % locals())
    return pd.Panel(dic)

def main(args):
    path = args[1]
    pf = list_files(path)
    print(pf.to_frame())
    return pf

if __name__ == '__main__':
    if len(sys.argv) > 1:
        pf = main(sys.argv)
