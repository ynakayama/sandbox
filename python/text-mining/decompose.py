import sys
import os
import MeCab


class Analyzer:

    def __init__(self, args):
        self.path = args[1]

    def tagger(self):
        return MeCab.Tagger('-d /usr/local/lib/mecab/dic/ipadic')

    def preprocessing(self, sentence):
        return sentence.rstrip()

    def get_nouns(self):
        tagger = self.tagger()
        with open(self.path) as fd:
            nouns = []
            for sentence in map(self.preprocessing, fd):
                for chunk in tagger.parse(sentence).splitlines()[:-1]:
                    (surface, feature) = chunk.split('\t')
                    if feature.startswith('名詞'):
                        nouns.append(surface)
        return nouns


if __name__ == '__main__':
    argsmin = 1
    version = (3, 0)
    if sys.version_info > (version):
        if len(sys.argv) > argsmin:
            analyzer = Analyzer(sys.argv)
            noun = analyzer.get_nouns()
            print(noun)
        else:
            print("This program needs at least %(argsmin)s arguments" %
                  locals())
    else:
        print("This program requires python > %(version)s" % locals())


