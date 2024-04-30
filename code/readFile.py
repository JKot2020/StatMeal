# readFile.py
# Reads .csv file

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp
import seaborn as sns
from IPython.display import HTML

def get_file(file):
    file_name = file
    return load_data(file_name)

def load_data(file_name):
    # read from .csv file
    receipt_data = pd.read_csv(open(file_name, encoding="utf-8", errors='ignore'), keep_default_na=False)

    my_path = os.path.abspath(__file__)
    # Remove "/readFile.py" from file path
    my_path = my_path[:-12]
    receipt_data.head().to_html(my_path + "/static/head.html")
    column_names = {"columns": receipt_data.columns}

    return column_names["columns"]