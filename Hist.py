# Richard Deegan
# Import Libraries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# First output required for project- Read iris CSV file to into DataFrame
iris = pd.read_csv("iris.csv")

#x = iris.sepal_length, 

# use Boolean logic to select rows and columns
setosa = iris.loc[iris["species"] == "setosa"]
versicolor = iris.loc[iris["species"] == "versicolor"]
virginica = iris.loc[iris["species"] == "virginica"]
#sepal_length = iris.sepal_length

setosa1 = setosa.sepal_length
plt.hist(setosa1)
plt.xlabel("Measurements in CM")
plt.ylabel("Frequency of Occurrence")
plt.title("Setosa Sepal Length")
plt.show()

setosa2 = setosa.sepal_width
plt.hist(setosa2)
plt.xlabel("Measurements in CM")
plt.ylabel("Frequency of Occurrence")
plt.title("Setosa Sepal Width")
plt.show()

setosa3 = setosa.petal_length
plt.hist(setosa3)
plt.xlabel("Measurements in CM")
plt.ylabel("Frequency of Occurrence")
plt.title("Setosa Petal Length")
plt.show()

setosa4 = setosa.petal_width
plt.hist(setosa4)
plt.xlabel("Measurements in CM")
plt.ylabel("Frequency of Occurrence")
plt.title("Setosa Petal Width")
plt.show()




#print (versicolor)
#print (virginica)

#References
#Data science, Startups, Analytics, and Data visualisation, https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/