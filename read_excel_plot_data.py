"""
This program opens Excel files, reads two columns of data titled 'column_x' 
and 'column_y' and creates a simple plot.
Created on Sat Oct 31 00:17:51 2020

@author: holmstead
"""

import matplotlib.pyplot as plt
plt.style.use('classic')
import pandas as pd
import numpy as np


path = "C:/Users/holmstead/Desktop/College/"        # has to be forward slash :|
filename = "test.xlsx"

title = "Time vs Temperature"
column_x = 'time'           # header of the column you want to read
column_y = 'temperature'
outf = "test.png"        # name of plot to save 


def read_excel(filename):
    '''
    this part reads the excel file. two columns are read and the data from 
    each are added to the empty lists
    '''
    x_values = []
    y_values = []
    df = pd.read_excel(path+filename)
    for i in df.index:
        x_values.append(df[column_x][i])
        y_values.append(df[column_y][i])
   return x_values, y_values
    
def make_plot():
    plt.plot(x_values, y_values, 'b')     # b is for blue line
    plt.xlabel(column_x)
    plt.ylabel(column_y)
    plt.title(title)
    # set axis range and increment:
    plt.xticks(np.arange(0, max(x_values), (max(x_values)/10)))    # start, stop, step 
    plt.yticks(np.arange(0, max(y_values), (max(y_values)/10)))
    plt.savefig(outf) # saves plot as given arguement (use .png)
    # n.b. have to save plot before display plot, else the file will be blank
    plt.show()  # displays plot to screen

# call the functions
read_excel(filename)
make_plot()
