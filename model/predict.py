import joblib
import pandas as pd
import numpy as np
import json

to_predict = pd.read_json(path)
to_predict = [to_predict['ndvi'], to_predict['temperature'], to_predict['rainfall']]

normalizer = joblib.load('normalizer.pkl')
to_predict = normalizer.transform(np.reshape(to_predict, (-1, 1))).T

model = joblib.load('locust_predict_model.pkl')

output = model.predict([to_predict.ravel()])

with open('result.json', 'w') as outfile:
    json.dump(output, outfile)
