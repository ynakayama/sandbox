# -*- coding: utf-8 -*-

import numpy as np
from sklearn.ensemble import RandomForestClassifier
import codecs

train_X = np.genfromtxt('train.csv', delimiter=',')
train_y = np.genfromtxt('trainLabels.csv', delimiter=',')
test_X  = np.genfromtxt('test.csv', delimiter=',')

clf = RandomForestClassifier()
clf.fit(train_X, train_y)

result = clf.predict(test_X)

def write_prediction(prediction, outfile):
    f = codecs.open(outfile, 'w')
    for x in prediction:
        f.write('%s\n' % (x))

write_prediction(result, 'random_forest.txt')

