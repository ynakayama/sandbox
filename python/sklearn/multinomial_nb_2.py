# -*- coding: utf-8 -*-

import numpy as np
from sklearn.naive_bayes import MultinomialNB

X = np.array([[1,2,3,4,5,6,7,8],
              [1,1,3,4,5,6,6,7],
              [2,1,2,4,5,8,8,8]])
y = np.array([1, 2, 3])

print(X)

# clf = MultinomialNB()
clf = MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
clf.fit(X, y)

_t = np.array([2,2,4,5,6,8,8,8])

print(_t)
print(clf.predict(_t))
