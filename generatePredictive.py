# generatePredictive.py
# Generates predictive model based on specified button prompt

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp
import seaborn as sns
import statsmodels.formula.api as smf
from pylab import *

# Generate regression model and return to web page
def make_regression(file_name, column_names):
    column_names = column_names[:-2]
    column_names = column_names.split(", ")

    receipt_data = pd.read_csv(open(file_name, encoding="utf-8", errors='ignore'), keep_default_na=False)
    mod = smf.ols(formula = "column_names[0] ~ column_names[1]", data = receipt_data.dropna())
    res = mod.fit()
    my_summary = res.summary()
    
    return my_summary