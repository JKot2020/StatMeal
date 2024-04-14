# generateGraph.py
# Generates graph based on specified button prompt

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp
import seaborn as sns

# auto
def make_auto():
    file_name = "Balaji Fast Food Sales.csv"
    receipt_data = pd.read_csv(file_name, keep_default_na=False)
    
    my_auto = sns.displot(data=receipt_data['item_name']).set(title='item_name')
    my_auto.set_xticklabels(rotation=45, horizontalalignment='right', fontweight='light', fontsize='large')
    plt.xlabel('item_name')

    return my_auto

# test
def test_graph(column_name, graph_name):
    return column_name