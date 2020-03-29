#Richard Deegan
#Import Libraries 
import numpy as np
import pandas as pd
import matplotlib as plt

#Read Iris CSV file to DataFrame- ref 1
df = pd.read_csv("iris.csv")

#Filter out the three main flowers for individual analysis- ref 2
setosa = df[df.species == "setosa"]
versicolor = df[df.species == "vericolor"]
virginica = df[df.species == "virginica"] 

df.head()




#references:
# Python Pandas read_csv – Load Data from CSV Files, https://www.shanelynn.ie/python-pandas-read_csv-load-data-from-csv-files/
# Data Science with Python: Intro to Loading, Subsetting, and Filtering Data with pandas https://towardsdatascience.com/data-science-with-python-intro-to-loading-and-subsetting-data-with-pandas-9f26895ddd7f