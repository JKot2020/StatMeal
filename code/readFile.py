# readFile.py
# Reads .csv file

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp
import seaborn as sns

def get_file(file):
    file_name = file
    return load_data(file_name)

def load_data(file_name):
    # read from .csv file
    receipt_data = pd.read_csv(open(file_name, encoding="utf-8", errors='ignore'), keep_default_na=False)

    column_names = {"columns": receipt_data.columns}

    return column_names["columns"]