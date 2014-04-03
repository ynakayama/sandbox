# -*- coding: utf-8 -*-

import numpy as np
from sklearn import svm
from sklearn import neighbors
from sklearn.ensemble import RandomForestClassifier
from sklearn import cross_validation
import codecs

train_X = np.genfromtxt('train.csv', delimiter=',')
train_y = np.genfromtxt('trainLabels.csv', delimiter=',')
test_X  = np.genfromtxt('test.csv', delimiter=',')

clf = svm.SVC()
scores = cross_validation.cross_val_score(clf, train_X, train_y, cv=5, n_jobs=1)
print( "SVM: %(scores)s" %locals() )
clf = neighbors.KNeighborsClassifier()
scores = cross_validation.cross_val_score(clf, train_X, train_y, cv=5, n_jobs=1)
print( "KNeighbors: %(scores)s" %locals() )
clf = RandomForestClassifier()
scores = cross_validation.cross_val_score(clf, train_X, train_y, cv=5, n_jobs=1)
print( "RandomForest: %(scores)s" %locals() )

