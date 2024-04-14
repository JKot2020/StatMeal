# generateGraph.py
# Generates graph based on specified button prompt

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp
import seaborn as sns

# filters given data to check which graph should be made
def sort_graph_data(file_name, column_names, graph_name):
    column_names = column_names[:-2]
    column_names = column_names.split(", ")

    if graph_name == "Auto-Select Graph":
        return make_auto(file_name, column_names, graph_name)

# auto
def make_auto(file_name, column_names, graph_name):
    receipt_data = pd.read_csv(file_name, keep_default_na=False)
    
    my_auto = sns.displot(data=receipt_data[column_names[0]]).set(title=graph_name)
    my_auto.set_xticklabels(rotation=45, horizontalalignment='right', fontweight='light', fontsize='large')
    my_auto.tight_layout()

    my_path = os.path.abspath(__file__)
    # Remove "/generateGraph.py" from file path
    my_path = my_path[:-17]
    my_auto.figure.savefig(my_path + "/static/output.png")

    return my_auto