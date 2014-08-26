
import numpy as np
import pandas as pd
rng = pd.date_range('1/1/2014', periods=100, freq='D')

df1 = pd.DataFrame(
    np.random.randn(100, 4), index=rng, columns=['A', 'B', 'C', 'D'])
df2 = pd.DataFrame(
    np.random.randn(100, 4), index=rng, columns=['A', 'B', 'C', 'D'])
df3 = pd.DataFrame(
    np.random.randn(100, 4), index=rng, columns=['A', 'B', 'C', 'D'])

pf = pd.Panel({'df1': df1, 'df2': df2, 'df3': df3})

print(pf.shape)

pf['df1']['E'] = pd.DataFrame(np.random.randn(100, 1), index=rng)
pf['df2']['E'] = pd.DataFrame(np.random.randn(100, 1), index=rng)

print(pf)
print(pf.ix['df1', -10:, 'E'])
