import pyper
import pandas as pd

wine = pd.read_csv("wine.csv")

# R のインスタンスを作る
r = pyper.R(use_pandas='True')

# Python 側のデータを R に渡す
r.assign("data", wine)

# R のソースコードを実行する
r("source(file='scatter.R')")

# R のコードを実行する
r("res1 = cor.test(data$WRAIN, data$LPRICE2)")
r("data1 = subset(data, LPRICE2 < 0)")
r("res2 = cor.test(data1$WRAIN, data1$LPRICE2)")

# Python で R のオブジェクトを読む
res1 = pd.Series(r.get("res1"))
print(res1)
res2 = pd.Series(r.get("res2"))
print(res2)
