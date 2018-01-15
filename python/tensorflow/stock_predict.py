# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

from sklearn import preprocessing
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.layers.recurrent import LSTM


class Prediction:

    def __init__(self):
        self.length_of_sequences = 10
        self.in_out_neurons = 1
        self.hidden_neurons = 300
        self.epochs = 100
        self.batch_size = 10

    def load_data(self, data, n_prev=10):
        X, Y = [], []
        for i in range(len(data) - n_prev):
            X.append(data.iloc[i:(i + n_prev)].as_matrix())
            Y.append(data.iloc[i + n_prev].as_matrix())
        retX = np.array(X)
        retY = np.array(Y)
        return retX, retY

    def create_model(self):
        model = Sequential()
        model.add(LSTM(self.hidden_neurons,
                       batch_input_shape=(None, self.length_of_sequences,
                                          self.in_out_neurons),
                       return_sequences=False))
        model.add(Dense(self.in_out_neurons))
        model.add(Activation("linear"))
        model.compile(loss="mape", optimizer="adam")
        return model

    def train(self, X_train, y_train):
        model = self.create_model()
        model.fit(X_train, y_train,
                  batch_size=self.batch_size,
                  epochs=self.epochs)
        return model


if __name__ == "__main__":

    prediction = Prediction()

    data = pd.read_csv('stock.csv').dropna(how='any')
    data.columns = ['date', 'open', 'high',
                    'low', 'close', 'volume', 'adj-close']
    data['date'] = pd.to_datetime(data['date'], format='%Y-%m-%d')
    scaled_data = data.copy()
    scaled_data['adj-close'] = preprocessing.scale(data['adj-close'])
    # data = data.sort_values(by='date')
    # scaled_data = scaled_data.reset_index(drop=True)
    scaled_data = scaled_data.loc[:, ['date', 'adj-close']]

    split_pos = int(len(scaled_data) * 0.8)
    x_train, y_train = prediction.load_data(
        scaled_data[['adj-close']].iloc[0:split_pos], prediction.length_of_sequences)
    x_test,  y_test = prediction.load_data(
        scaled_data[['adj-close']].iloc[split_pos:], prediction.length_of_sequences)

    model = prediction.train(x_train, y_train)

    predicted = model.predict(x_test)

    result = pd.DataFrame(predicted)
    result.columns = ['predict']
    result['actual'] = y_test
    result.plot()
    plt.show()
    plt.savefig("image.png")
