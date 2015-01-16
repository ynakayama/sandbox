import pandas as pd
import statsmodels.api as sm
from matplotlib import pyplot as plt
from matplotlib import font_manager

prop = font_manager.FontProperties(
    fname="/usr/share/fonts/truetype/fonts-japanese-gothic.ttf")

stock_9682 = pd.read_csv('stock_9682.csv',
                         parse_dates=True, index_col=0)
stock_9613 = pd.read_csv('stock_9613.csv',
                         parse_dates=True, index_col=0)
stock_3626 = pd.read_csv('stock_3626.csv',
                         parse_dates=True, index_col=0)
stock_9759 = pd.read_csv('stock_9759.csv',
                         parse_dates=True, index_col=0)

df = pd.DataFrame([
    stock_9613.ix['2010-01-01':, '終値'],
    stock_9682.ix['2010-01-01':, '終値'],
    stock_3626.ix['2010-01-01':, '終値'],
    stock_9759.ix['2010-01-01':, '終値']
], index=['NTT データ', 'DTS', 'IT ホールディングス', 'NSD']).T

rets = df.pct_change().dropna()
by_year = rets.groupby(lambda x: x.year)
vol_corr = lambda x: x.corrwith(x['NTT データ'])

result1 = by_year.apply(vol_corr)

print(result1)

plt.figure()
result1.plot()
plt.legend(prop=prop)
plt.xticks([2010, 2011, 2012, 2013, 2014, 2015])
plt.xlabel('年', fontproperties=prop)
plt.show()
plt.savefig("image.png")
plt.close()

result2 = by_year.apply(lambda g: g['DTS'].corr(g['NTT データ']))

print(result2)

def regression(data, yvar, xvars):
    Y = data[yvar]
    X = data[xvars]
    X['intercept'] = 1.
    result = sm.OLS(Y, X).fit()
    return result.params

result3 = by_year.apply(regression, 'DTS', ['NTT データ'])

print(result3)
