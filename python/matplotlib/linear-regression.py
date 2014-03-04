# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

v1 = np.array([24, 27, 29, 34, 42, 43, 51])
v2 = np.array([236, 330, 375, 392, 460, 525, 578])

def phi(x):
    return [1, x, x**2, x**3]

def f(w, x):
    return np.dot(w, phi(x))

PHI = np.array([phi(x) for x in v2])
w = np.linalg.solve(np.dot(PHI.T, PHI), np.dot(PHI.T, v1))

plt.xlim(20, 55)
plt.ylim(200, 600)
plt.xlabel('Age')
plt.ylabel('Price')
plt.plot(v1, v2, 'o', color="blue")
plt.show()
plt.savefig("image.png")

ylist = np.arange(200, 600, 10)
xlist = [f(w, x) for x in ylist]

plt.plot(xlist, ylist, color="red")
plt.xlim(20, 55)
plt.ylim(200, 600)
plt.xlabel('Age')
plt.ylabel('Price')
plt.plot(v1, v2, 'o', color="blue")
plt.show()
plt.savefig("image2.png")

