import sys
import os
import MeCab
import pandas as pd

class Analyzer:

    def __init__(self, args):
        self.path = args[1]

    def tagger(self):
        return MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')

    def preprocessing(self, sentence):
        return sentence.rstrip()

    def get_nouns(self):
        tagger = self.tagger()
        columns = ['surface', 'speech', 'subclass1', 'subclass2', 'subclass3', 'conjugation_type', 'conjugation_form', 'prototype', 'reading', 'pronunciation']
        df = pd.DataFrame(index=[], columns=columns)
        with open(self.path) as fd:
            for sentence in map(self.preprocessing, fd):
                for chunk in tagger.parse(sentence).splitlines()[:-1]:
                    (surface, feature) = chunk.split('\t')
                    speech, subclass1, subclass2, subclass3, conjugation_type, conjugation_form, prototype, reading, pronunciation = feature.split(',')
                    record = pd.Series([surface, speech, subclass1, subclass2, subclass3, conjugation_type, conjugation_form, prototype, reading, pronunciation], index=df.columns)
                    df = df.append(record, ignore_index=True)
        return df


if __name__ == '__main__':
    argsmin = 1
    version = (3, 0)
    if sys.version_info > (version):
        if len(sys.argv) > argsmin:
            analyzer = Analyzer(sys.argv)
            df = analyzer.get_nouns()
            print(df.surface.head(10))
            print(df.speech.head(10))
            print(df.subclass1.head(10))
        else:
            print("This program needs at least %(argsmin)s arguments" %
                  locals())
    else:
        print("This program requires python > %(version)s" % locals())


