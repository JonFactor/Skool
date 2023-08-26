### imports
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import utils
### code
data = pd.read_csv('Backups\MANUAL-FAILSAFE\\ai\my own\APPL.csv')
opens = []
for l in data['Open']:
    opens.append(l)
y = 1
x = 0
diffrence = []
diffrencetf = []
while y < len(opens):
    diff = ((opens[x] - opens[y]) / opens[y]) * 100
    if diff < 0:
        diffrencetf.append(False)
    else:
        diffrencetf.append(True)
    diff2 = ((opens[y] - opens[x]) / opens[x]) * 100
    if diff2 < 0:
        diffrencetf.append(False)
    else:
        diffrencetf.append(True)
    diffrence.append(float(diff2))
    diffrence.append(float(diff))
    x += 2
    y += 2
data['Change'] = diffrence
badcomma = []
for vol in data['Volume']:
    badcomma.append(vol.replace(',', ''))
data['Volume'] = badcomma
x = data.drop(columns=['Change', 'Date', 'Volume'])
y = data['Change']


lab = preprocessing.LabelEncoder()
y_transformed = lab.fit_transform(y)

x_Train, x_test, y_train, y_test = train_test_split(x, y_transformed, test_size=.2)
model = DecisionTreeClassifier()
model.fit(x_Train, y_train)
prediction = model.predict(x_test)

score = accuracy_score(y_test, prediction)

print(data, score)