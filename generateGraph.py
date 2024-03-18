# generateGraph.py
# Generates graph based on specified button prompt

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp
import seaborn as sns

# histogram
def make_hist():
    file_name = "Balaji Fast Food Sales.csv"
    receipt_data = pd.read_csv(file_name, keep_default_na=False)
    
    my_hist = sns.displot(data=receipt_data['item_name']).set(title='item_name')
    my_hist.set_xticklabels(rotation=45, horizontalalignment='right', fontweight='light', fontsize='large')
    plt.xlabel('item_name')
    plt.ylabel('Frequency')

    return my_hist