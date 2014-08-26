
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

def linreg(a, b):
    slope, intercept, r_value, p_value, std_err = stats.linregress(a, b)
    print(slope, intercept, r_value, p_value, std_err)

linreg(x, z)
linreg(y, z)
