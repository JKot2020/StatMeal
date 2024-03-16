# readFile.py
# Reads .csv file

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp
import seaborn as sns

def get_file(file_name):
    # Temp line for testing purposes
    file_name = "Balaji Fast Food Sales.csv"
    load_data(file_name)

def load_data(file_name):
    # read from .csv file
    survey_data = pd.read_csv(file_name, keep_default_na=False)
    
    # create dataframe
    data_combined = pd.DataFrame(survey_data)