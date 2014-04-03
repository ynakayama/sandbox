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

def get_score(clf, train_features, train_labels):
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(train_features, train_labels, test_size=0.4, random_state=0)
    clf.fit(X_train, y_train)
    return clf.score(X_test, y_test)

clf = svm.SVC()
scores = get_score(clf, train_X, train_y)
print( scores )

clf = svm.SVC(C=100, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.001, kernel="rbf", max_iter=-1, probability=False,random_state=None, shrinking=True, tol=0.001, verbose=False)
scores = get_score(clf, train_X, train_y)
print( scores )

