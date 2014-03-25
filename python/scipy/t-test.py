import numpy as np
import scipy as sp
from scipy import stats

X = np.random.randint(65, 90, size=8)
Y = np.random.randint(75, 95, size=8)

print(X)
print(Y)

t, p = stats.ttest_rel(X, Y)

print( "t 値は %(t)s" %locals() )
print( "確率は %(p)s" %locals() )

if p < 0.05:
    print("有意な差があります")
else:
    print("有意な差がありません")

