import pandas as pd
import sys
import numpy as np
from imblearn.over_sampling import RandomOverSampler
from sklearn.preprocessing import Normalizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import joblib

X = pd.read_csv(sys.argv[0])

cops = pd.read_csv(sys.argv[1])
month_period = {i + 1: (item, item + 1, item + 2) for i, item in enumerate(np.arange(1, 36, 3))}
cops['LOCNAME'] = cops['LOCNAME'].str.lower()


def GetY(place):
    dates = [item.split()[0].split('-') for item in cops[cops['LOCNAME'].str.contains(place)]['STARTDATE']]
    dates = np.array(dates)
    dates = list([(int(np.floor(int(item[0]) / 11)), int(item[1]), int(item[2])) for item in dates])
    index = []
    for item in dates:
        df = X[(X['location'] == place) & (X['year'] == item[-1]) & (X['period'] == month_period[item[1]][item[0]])]
        if len(df) != 0:
            index.append(df.index[0])
    return index


y = np.zeros(len(X))
_index = []
for item in X.location.unique():
    _index.extend(GetY(item))

for item in _index:
    y[item] = 1


X.drop(['period', 'location', 'year'], axis=1, inplace=True)

normalizer = Normalizer()
X = normalizer.fit_transform(X.T).T
joblib.dump(normalizer, 'normalizer.pkl')

ros = RandomOverSampler()
X, y = ros.fit_resample(X, y)

xtr, xte, ytr, yte = train_test_split(X, y, stratify=y)

model = DecisionTreeClassifier()
model.fit(xtr, ytr)
joblib.dump(model, 'locust_predict_model.pkl')