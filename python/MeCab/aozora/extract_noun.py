import sys
import MeCab

tagger = MeCab.Tagger('-d /usr/local/lib/mecab/dic/ipadic')

def preprocessing(sentence):
    return sentence.rstrip()

def extract_noun_by_parse(path):
    with open(path) as fd:
        nouns = []
        for sentence in map(preprocessing, fd):
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
            noun = extract_noun_by_parse(sys.argv[1])
            print(len(noun))
        else:
            print("This program needs at least %(argsmin)s arguments" %
                  locals())
    else:
        print("This program requires python > %(version)s" % locals())
