# -*- coding: utf-8 -*-

# Data Science London + Scikit-learn
# DataSet: https://www.kaggle.com/c/data-science-london-scikit-learn/data?test.csv
# Code: http://codiply.com/blog/data-science-london-scikit-learn-kaggle-competition-part-i

import numpy as np
from sklearn import svm, cross_validation
import codecs

train_X = np.genfromtxt('train.csv', delimiter=',')
train_y = np.genfromtxt('trainLabels.csv', delimiter=',')
test_X  = np.genfromtxt('test.csv', delimiter=',')

def get_model(tr_X, tr_y):
    svc = svm.SVC(C=1, kernel='rbf')
    svc.fit(train_X, train_y)
    return svc

def test_model():
    k_fold = cross_validation.KFold(len(train_X), n_folds=10, indices=True)
    scores = []
    for train_indices, test_indices in k_fold:
        model = get_model(train_X[train_indices], train_y[train_indices])
        score = model.score(train_X[test_indices], train_y[test_indices])
        scores.append(score)
    print(min(scores), sum(scores)/len(scores), max(scores))

def save_predictions(filename):
    model = get_model(train_X, train_y)
    prediction = [ int(x) for x in model.predict(test_X) ]
    write_prediction(prediction, filename)

def write_prediction(prediction, outfile):
    f = codecs.open(outfile, 'w')
    for x in prediction:
        f.write('%s\n' % (x))

test_model()
save_predictions('svm.txt')

