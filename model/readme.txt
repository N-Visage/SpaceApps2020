data_build.py:
running this file creates a dataset used for model prediction
args:
    temperature data folder path
    rainfall data folder path
    ndvi data folder path

model.py
running this file builds the decision tree model used for prediction
args:
    file path of the dataset saved
    file path of the control operations dataset

predict.py
this script reads the user given data and predict whether the palce is likely to get infected by locusts or not