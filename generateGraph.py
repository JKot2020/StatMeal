# generateGraph.py
# Generates graph based on specified button prompt

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp
import seaborn as sns
from pylab import *

# filters given data to check which graph should be made
def sort_graph_data(file_name, column_names, graph_name):
    column_names = column_names[:-2]
    column_names = column_names.split(", ")

    if graph_name == "Distribution Plot":
        return make_dist(file_name, column_names, graph_name)
    if graph_name == "Box Plot":
        return make_box(file_name, column_names, graph_name)
    if graph_name == "Histogram":
        return make_hist(file_name, column_names, graph_name)
    if graph_name == "Line Graph":
        return make_line(file_name, column_names, graph_name)
    if graph_name == "Pie Chart":
        return make_pie(file_name, column_names, graph_name)

# make distribution graph
def make_dist(file_name, column_names, graph_name):
    receipt_data = pd.read_csv(file_name, keep_default_na=False)
    
    # Check if there is both an x and y variable
    if (len(column_names) > 1):
        my_dist = sns.displot(data=receipt_data, x=column_names[0], y=column_names[1]).set(title=graph_name)
    else:
        my_dist = sns.displot(data=receipt_data[column_names[0]]).set(title=graph_name)
    my_dist.set_xticklabels(rotation=45, horizontalalignment='right', fontweight='light', fontsize='large')
    my_dist.tight_layout()

    my_path = os.path.abspath(__file__)
    # Remove "/generateGraph.py" from file path
    my_path = my_path[:-17]
    my_dist.figure.savefig(my_path + "/static/output.png")

    return my_dist

# make boxplot
def make_box(file_name, column_names, graph_name):
    receipt_data = pd.read_csv(file_name, keep_default_na=False)
    #TODO parse column_names more to allow for more box plots
    my_box = plt.boxplot(data=receipt_data, x=column_names[0])
    my_box = plt.xticks(rotation=45)
    my_box = plt.suptitle(graph_name)
    my_box = plt.tight_layout()

    my_path = os.path.abspath(__file__)
    # Remove "/generateGraph.py" from file path
    my_path = my_path[:-17]
    my_box = plt.savefig(my_path + "/static/output.png")

    return my_box

# make histogram
def make_hist(file_name, column_names, graph_name):
    receipt_data = pd.read_csv(file_name, keep_default_na=False)
    
    my_hist = sns.histplot(receipt_data[column_names])
    my_hist = plt.xticks(rotation=45)
    my_hist = plt.tight_layout()

    my_path = os.path.abspath(__file__)
    # Remove "/generateGraph.py" from file path
    my_path = my_path[:-17]
    my_hist = plt.savefig(my_path + "/static/output.png")

    return my_hist

#TODO Fix line graph variables
# make line graph
def make_line(file_name, column_names, graph_name):
    receipt_data = pd.read_csv(file_name, keep_default_na=False)
    
    my_line = plt.plot(receipt_data[column_names[0]], receipt_data[column_names[1]])
    my_line = plt.title(graph_name)
    my_line = plt.xlabel(column_names[0])
    my_line = plt.ylabel(column_names[1])
    my_line = plt.tight_layout()

    my_path = os.path.abspath(__file__)
    # Remove "/generateGraph.py" from file path
    my_path = my_path[:-17]
    my_line = plt.savefig(my_path + "/static/output.png")

    return my_line

# make pie chart
def make_pie(file_name, column_names, graph_name):
    receipt_data = pd.read_csv(file_name, keep_default_na=False)
    
    my_pie = receipt_data[column_names[0]].value_counts(dropna=False).plot.pie(autopct='%1.1f%%')
    my_pie = plt.axis('equal')

    my_path = os.path.abspath(__file__)
    # Remove "/generateGraph.py" from file path
    my_path = my_path[:-17]
    my_pie = plt.savefig(my_path + "/static/output.png")

    return my_pie