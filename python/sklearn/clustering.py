#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
import codecs
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans, MiniBatchKMeans
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import Normalizer

class Analyzer:
    def __init__(self, args):
        self.infile = args[1]
        self.outfile = args[2]
        self.num_clusters = 5
        self.lsa_dim = 500
        self.max_df = 0.8
        self.max_features = 10000
        self.minibatch = True

    def _read_from_file(self):
        list = []
        file = open(self.infile, 'r')
        for line in file:
            list.append( line.rstrip() )
        file.close
        return list

    def make_cluster(self):
        texts = self._read_from_file()
        print("texts are %(texts)s" %locals() )

        vectorizer = TfidfVectorizer(max_df=self.max_df, max_features=self.max_features, stop_words='english')
        X = vectorizer.fit_transform(texts)
        print("X values are %(X)s" %locals() )

        if self.minibatch:
            km = MiniBatchKMeans(n_clusters=self.num_clusters, init='k-means++', batch_size=1000, n_init=10, max_no_improvement=10, verbose=True)
        else:
            km = KMeans(n_clusters=self.num_clusters, init='k-means++', n_init=1, verbose=True)
        km.fit(X)
        labels = km.labels_

        transformed = km.transform(X)
        dists = np.zeros(labels.shape)
        for i in range(len(labels)):
            dists[i] = transformed[i, labels[i]]

        clusters = []
        for i in range(self.num_clusters):
            cluster = []
            ii = np.where(labels==i)[0]
            dd = dists[ii]
            di = np.vstack([dd,ii]).transpose().tolist()
            di.sort()
            for d, j in di:
                cluster.append(texts[int(j)])
            clusters.append(cluster)

        return clusters

    def write_cluster(self, clusters):
        f = codecs.open('%s' % self.outfile, 'w', 'utf-8')
        for i, texts in enumerate(clusters):
            for text in texts:
                f.write('%d: %s\n' % (i, text.replace('/n', '')))

if __name__ == '__main__':
    if sys.version_info > (3,0):
        if len(sys.argv) > 2:
            analyzer = Analyzer(sys.argv)
            clusters = analyzer.make_cluster()
            print("Result clusters are %(clusters)s" %locals() )
            analyzer.write_cluster(clusters)

        else:
            print("Invalid arguments")
    else:
        print("This program require python > 3.0")

