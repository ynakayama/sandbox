from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
# from pylab import plot,show,hist,figure,title
import pylab as plb

# picking 500 of from a normal distrubution
# with mean 0 and standard deviation 1
# x = np.sort(np.random.uniform(-np.pi, np.pi,100))
# y = np.sin(x) + 0.1*np.random.normal(size=len(x))
# samp = y
sample = norm.rvs(loc=100,scale=1,size=500)
#samp = np.sort(np.random.randint(65, 90, size=8))

param = norm.fit(sample) # distribution fitting

print (sample)
print (param)

# now, param[0] and param[1] are the mean and 
# the standard deviation of the fitted distribution
x = np.linspace(95,105,100)
# fitted distribution
pdf_fitted = norm.pdf(x,loc=param[0],scale=param[1])
# original distribution
pdf = norm.pdf(x)

plt.figure
plt.title('Normal distribution')

plt.plot(x, pdf_fitted, 'r-', x,pdf, 'b-')
plt.hist(sample, normed=1, alpha=.3)

plt.show()
plt.savefig("image.png")

