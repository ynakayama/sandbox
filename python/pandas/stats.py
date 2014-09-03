
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv", names=['X', 'Y', 'Z'])
print(data.describe())

from pandas.tools.plotting import scatter_matrix
plt.figure()
scatter_matrix(data)
plt.savefig("image.png")

print(data.corr())

x = data.ix[:, 0].values
y = data.ix[:, 1].values
z = data.ix[:, 2].values

linreg = lambda a, b: stats.linregress(a, b)

slope, intercept, r_value, p_value, std_err = linreg(x, z)
print(slope, intercept, r_value, p_value, std_err)

print(linreg(y, z))
