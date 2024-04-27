# generatePredictive.py
# Generates predictive model based on specified button prompt

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp
import seaborn as sns
import statsmodels.api as smf
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor
from pylab import *

# Generate regression model and return to web page
def make_regression(file_name, column_names):
    column_names = column_names[:-2]
    column_names = column_names.split(", ")

    receipt_data = pd.read_csv(open(file_name, encoding="utf-8", errors='ignore'), keep_default_na=False)
    Y, X = receipt_data[column_names[0]], receipt_data[column_names[0:]]
    my_model = smf.OLS(Y, X)
    res = my_model.fit()

    my_path = os.path.abspath(__file__)
    # Remove "/generatePredictive.py" from file path
    my_path = my_path[:-21]
    text_file = open(my_path + "/static/Regression.txt", "w")
    text_file.write(res.summary().as_text())
    text_file.close()
    
    return text_file

# Generate predictive model based on model
def make_predictive(file_name, column_names):
    column_names = column_names[:-2]
    column_names = column_names.split(", ")

    receipt_data = pd.read_csv(open(file_name, encoding="utf-8", errors='ignore'), keep_default_na=False)

    # features and target for given model
    features = receipt_data[column_names[0:]]
    target = receipt_data[column_names[0]]

    # Append target and feature variables
    Y, X = receipt_data[target], receipt_data[features]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

    # create model using the RandomForestRegressor model
    predict_model = RandomForestRegressor(n_estimators=100, max_depth=2, min_samples_split=3, min_samples_leaf=2, random_state=42)

    # train the predict_model
    predict_model.fit(X_train, Y_train)

    # create predictions
    Y_predict = predict_model.predict(X_test)

    # calculate MSE and r2 value
    mse = mean_squared_error(Y_test, Y_predict)
    r2 = r2_score(Y_test, Y_predict)

    print(f'MSE: {mse}')
    print(f'R-squared: {r2 * 100}')

    # Clean plot beforehand
    plt.clf()

    # generate scatter plot for actual vs predicted values
    my_predict_model = plt.scatter(X_test[column_names[0:]], Y_test, label='Actual Values')
    sorted_indices = X_test[column_names[0:]].squeeze().argsort()
    my_predict_model = plt.scatter(X_test[column_names[0:]].iloc[sorted_indices], Y_predict[sorted_indices], label='Predicted Values')
    my_predict_model = plt.title('Actual vs Predicted')
    my_predict_model = plt.xlabel('Mean')
    my_predict_model = plt.ylabel('Features')
    my_predict_model = plt.legend()
    
    my_path = os.path.abspath(__file__)
    # Remove "/generatePredictive.py" from file path
    my_path = my_path[:-21]
    my_predict_model.figure.savefig(my_path + "/static/Predictive_Model.png")

    return my_predict_model