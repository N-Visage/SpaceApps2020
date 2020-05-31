import pandas as pd
import numpy as np
import os
import sys



def GetData(path):
    data = pd.read_csv(path)
    if 'Unnamed: 4' in data:
        data.drop(['Unnamed: 4'], axis=1, inplace=True)
    data.drop(['Month'], axis=1, inplace=True)
    data.dropna(inplace=True)
    data['location'] = [path.split('/')[-1].split('_')[0]] * len(data)
    return data


def Reshape(df):
    year1 = int(df.columns[1].split('-')[0])
    year2 = int(df.columns[2].split('-')[0])
    return pd.DataFrame(np.vstack([[[df.iloc[i][0], df.iloc[i][1], year1, df.iloc[i][-1]] for i in range(len(df))],
                                   [[df.iloc[i][0], df.iloc[i][2], year2, df.iloc[i][-1]] for i in range(len(df))]]))


def Combine(ndvi, temp, rainfall):
    data = ndvi.merge(temp, on=(0, 2, 3))
    data = data.merge(rainfall, on=(0, 2, 3))
    cols = ['period', 'ndvi', 'year', 'location', 'temp', 'rainfall']
    data.columns = cols
    return data


def Function(folder):
    f = ['{}/{}'.format(root, item) for (root, _, files) in os.walk(folder) for item in files]
    for item in f:
        _temp = Reshape(GetData(item))
    return pd.DataFrame(np.vstack([Reshape(GetData(item)).dropna() for item in f]))


temperature = Function("data/data/temperature")
rainfall = Function("data/data/rainfall")
ndvi = Function("data/data/ndvi")

X = Combine(ndvi, temperature, rainfall)
X['year'] = X['year'].astype(int)
X['period'] = X['period'].astype(int)

X.to_csv("data_build.csv")
