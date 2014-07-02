# -*- coding: utf-8 -*-

import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data = np.genfromtxt('CodeIQ_data.txt', delimiter=' ')
eaten = np.genfromtxt('CodeIQ_eaten.txt', delimiter=' ')

def kmeans(features):
    kmeans_model = KMeans(n_clusters=3, random_state=10).fit(features)
    labels = kmeans_model.labels_
    return labels

def plot(data, eaten):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    x1, y1 = np.array([[x[0], x[1]] for x in data]).T
    ax.scatter(x1, y1, color='b')
    x2, y2 = np.array([[x[0], x[1]] for x in eaten if x[2] == 1]).T
    ax.scatter(x2, y2, color='r')
    x3, y3 = np.array([[x[0], x[1]] for x in eaten if x[2] == 0]).T
    ax.scatter(x3, y3, color='g')
    plt.legend(loc='best')
    plt.show()
    plt.savefig("image.png")

plot(data, eaten)
labels = kmeans(data)

for label, feature in zip(labels, data):
    print(label, feature)

