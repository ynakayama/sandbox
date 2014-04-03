# -*- coding: utf-8 -*-

import numpy as np
from sklearn.grid_search import GridSearchCV
from sklearn import svm

train_X = np.genfromtxt('train.csv', delimiter=',')
train_y = np.genfromtxt('trainLabels.csv', delimiter=',')

tuned_params = [
        {'C':[1,10,100,1000], 'kernel':['linear']},
        {'C':[1,10,100,1000], 'gamma':[0.001, 0.0001], 'kernel':['rbf']},
        ]
clf = GridSearchCV(svm.SVC(C=1), tuned_params, n_jobs=-1)

clf.fit(train_X, train_y, cv=5)
best = clf.best_estimator_
print( "Best is %(best)s" %locals() )

