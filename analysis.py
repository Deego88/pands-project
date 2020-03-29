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

# create sepal length table, 
print ("This is the Sepal Length Table")
Sepal_length_Table =  pd.DataFrame(np.array([[np.min(setosa["Sepal_length"],[np.max(setosa["Sepal_length"],[np.std(setosa["Sepal_length"],[np.median(setosa["Sepal_length"],[np.sum(setosa["Sepal_length"])],
                        [np.min(versicolor["Sepal_length"],[np.max(versicolor["Sepal_length"],[np.std(versicolor["Sepal_length"],[np.median(versicolor["Sepal_length"],[np.sum(versicolor["Sepal_length"])],
                        [np.min(virginica["Sepal_length"],[np.max(virginica["Sepal_length"],[np.std(virginica["Sepal_length"],[np.median(virginica["Sepal_length"],[np.sum(virginica["Sepal_length"])]
print(Sepal_length_Table)

print ("This is the Sepal Width Table")


print ("This is thePetal Length Table")


print ("This is thePetal Width Table")


#references:
# Python Pandas read_csv – Load Data from CSV Files, https://www.shanelynn.ie/python-pandas-read_csv-load-data-from-csv-files/
# Data Science with Python: Intro to Loading, Subsetting, and Filtering Data with pandas https://towardsdatascience.com/data-science-with-python-intro-to-loading-and-subsetting-data-with-pandas-9f26895ddd7f
# ,https://jakevdp.github.io/PythonDataScienceHandbook/02.04-computation-on-arrays-aggregates.html