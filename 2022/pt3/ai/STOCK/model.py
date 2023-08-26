### imports
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
import tensorflow
### varibles
## user
from firstTimeSetup import user
## ticker
from getdata import strtick
### import data
df = pd.read_csv(f"C:\\Users\{user}\Desktop\Stocks\data\{strtick}.csv", header=None)
### data cleaning
## delete unnecessary
del df[6]
del df[5]
## make tmrw price column
finalresult = [0]
def tmrw():
    x = 1
    while x < len(df):
        num = df.iloc[x][0]
        finalresult.append(float(num))

        x += 1
tmrw()
del finalresult[0]
finalresult.append(140)
df['Result'] = finalresult
### model
## set input and output
x = df['Result']
y = df.drop(columns='Result')
## set train and tests
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
## define model
model = tensorflow.keras.models.Sequential()
## add layers
model.add(tensorflow.keras.layers.Dense(100, input_shape=x_train.shape, activation='sigmoid'))
model.add(tensorflow.keras.layers.Dense(100, activation='sigmoid'))
model.add(tensorflow.keras.layers.Dense(1, activation='sigmoid'))
## complie model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
## fit model
model.fit(x_train, y_train, epochs=100)

