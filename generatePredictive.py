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
def make_predictive():
    return