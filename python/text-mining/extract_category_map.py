#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import json
import re
from collections import OrderedDict

class Analyzer:

    def __init__(self, args):
        self.filename = args[1]
        self.exclude = args[2]
        self.exclude_list = []
        self.category_num = 0

    def start(self):
        self._read_from_exclude()
        self._extract_map('category.social')
        self._extract_map('category.politics')
        self._extract_map('category.international')
        self._extract_map('category.economics')
        self._extract_map('category.electro')
        self._extract_map('category.sports')
        self._extract_map('category.entertainment')
        self._extract_map('category.science')

    def _output(self, key, tag, value):
        print(key, tag, json.dumps(value, ensure_ascii=False), sep="\t")

    def _extract_map(self, category):
        self.dic = OrderedDict()
        file = open(self.filename, 'r')
        for line in file:
            word, counts, social, politics, international, economics, electro, sports, entertainment, science, standard_deviation = line.rstrip(
            ).split("\t")
            array = [int(social), int(politics), int(international), int(
                economics), int(electro), int(sports), int(entertainment), int(science)]
            if not array[self.category_num] == 0:
                if float(standard_deviation) < 10.0:
                    if not word in self.exclude_list:
                        r = re.compile("[一-龠]")
                        if r.match(word):
                            self._add_dic(word, array[self.category_num] * 3)
                        else:
                            self._add_dic(word, array[self.category_num])

        file.close
        self.category_num += 1
        self._output(self.category_num, category, self.dic)
        return self.dic

    def _add_dic(self, word, count):
        if word in self.dic:
            self.dic[word] += count
        else:
            self.dic[word] = count

    def _read_from_exclude(self):
        file = open(self.exclude, 'r')
        for line in file:
            self.exclude_list.append(line.rstrip())
        file.close
        return self.exclude_list

if __name__ == '__main__':
    argsmin = 2
    version = (3, 0)
    if sys.version_info > (version):
        if len(sys.argv) > argsmin:
            analyzer = Analyzer(sys.argv)
            analyzer.start()
        else:
            print("This program needs at least %(argsmin)s arguments" %
                  locals())
    else:
        print("This program requires python > %(version)s" % locals())
