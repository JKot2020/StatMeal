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

    combined_features = column_names[0:]
    target = column_names[0]

    # seperate of features and target
    X = receipt_data[combined_features]
    y = receipt_data[target]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # create combined_model using the RandomForestRegressor model
    combined_model = RandomForestRegressor(n_estimators=100, max_depth=2, min_samples_split=3, min_samples_leaf=2, random_state=42)

    # train combined_model
    combined_model.fit(X_train, y_train)

    # create predictions
    y_pred = combined_model.predict(X_test)

    # calculate MSE and r2 value
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f'MSE: {mse}')
    print(f'R-squared: {r2 * 100}')

    # calculate mean for all means test set
    X_test['combined_feat'] = X_test[column_names[0:]].mean(axis=1)

    # Clean plot beforehand
    plt.clf()

    # scatter plot for actual vs predicted grip strength for all means
    my_predict_model = plt.scatter(X_test['combined_feat'], y_test, label='Actual Values')
    sorted_indices = X_test['combined_feat'].squeeze().argsort()
    plt.scatter(X_test['combined_feat'].iloc[sorted_indices], y_pred[sorted_indices], label='Predicted Values')
    plt.title('Actual vs Predicted Grip Strength (Combined Personal Inventory)')
    plt.xlabel('Combined Personal Inventory of All Means')
    plt.ylabel('Grip Strength')
    plt.legend()
    
    my_path = os.path.abspath(__file__)
    # Remove "/generatePredictive.py" from file path
    my_path = my_path[:-21]
    my_predict_model.figure.savefig(my_path + "/static/Predictive_Model.png")

    return my_predict_model