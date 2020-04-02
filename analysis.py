# Richard Deegan
# Import Libraries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read Iris CSV file to into the Pandas DataFrame
iris = pd.read_csv("iris.csv")

# create variables head and tail, initial look at data set 1st 10 and last 10 lines.
head = iris.head()
tail = iris.tail()

print ("the first ten lines of the iris data set are:", head)
print ("the last ten lines of the iris data set are:", tail)

# references:
# 1. Python Pandas read_csv – Load Data from CSV Files, https://www.shanelynn.ie/python-pandas-read_csv-load-data-from-csv-files/
# 2. Data Science with Python: Intro to Loading, Subsetting, and Filtering Data with pandas https://towardsdatascience.com/data-science-with-python-intro-to-loading-and-subsetting-data-with-pandas-9f26895ddd7f
# 3. Aggregations, Min, Max, and Everything In Between,https://jakevdp.github.io/PythonDataScienceHandbook/02.04-computation-on-arrays-aggregates.html