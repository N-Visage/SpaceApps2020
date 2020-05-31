import joblib
import pandas as pd
import numpy as np
import json


class LAD:

    def __init__(self):
        pass

    def predict_results(self, to_predict):
        normalizer = joblib.load('norm.pkl')
        model = joblib.load('dt_model.pkl')
        to_predict = np.reshape(np.array(to_predict), (-1, 1))
        to_predict = normalizer.transform(to_predict)
        output = model.predict([to_predict.ravel()])
        file = open('result.txt', 'w')
        file.write(str(output[0]))
