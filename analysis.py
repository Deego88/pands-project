# Richard Deegan
# Import Libraries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read Iris CSV file to into the Pandas DataFrame
iris = pd.read_csv("iris.csv")

# create variables and print to screen, initial look at data set. 
head = iris.head()
tail = iris.tail()
describe = iris.describe()
mean = iris.mean()

#print to screen, stastics for initial observations. Describe function is very useful in this regard.  
print ("the first ten lines of the iris data set are:", head)
print ("the last ten lines of the iris data set are:", tail)
print ("a description of the iris data set:", describe)
print ("The mean of the iris data set is:", mean)

#Histogram for Sepal length variable 1
plt.figure(figsize = (10, 7)) 
x = data ["SepalLengthCm"] 
  
plt.hist(x, bins = 15, color = "blue") 
plt.title("Sepal Length in cm") 
plt.xlabel("Sepal_Length_cm") 
plt.ylabel("Count") 

plt.show()

#Histogram for Sepal width variable 2
plt.figure(figsize = (10, 7)) 
x = data.SepalWidthCm 
  
plt.hist(x, bins = 15, color = "blue") 
plt.title("Sepal Width in cm") 
plt.xlabel("Sepal_Width_cm") 
plt.ylabel("Count") 
  
plt.show() 

#Histogram for Petal length variable 3







# references:
# 1. Python Pandas read_csv – Load Data from CSV Files, https://www.shanelynn.ie/python-pandas-read_csv-load-data-from-csv-files/
# 2. Data Science with Python: Intro to Loading, Subsetting, and Filtering Data with pandas https://towardsdatascience.com/data-science-with-python-intro-to-loading-and-subsetting-data-with-pandas-9f26895ddd7f
# 3. Aggregations, Min, Max, and Everything In Between,https://jakevdp.github.io/PythonDataScienceHandbook/02.04-computation-on-arrays-aggregates.html