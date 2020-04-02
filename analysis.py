# Richard Deegan
# Import Libraries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# First output required for project- Read iris CSV file to into DataFrame
iris = pd.read_csv("iris.csv")

# create variables and print to screen, initial look at data set. 
head = iris.head()
tail = iris.tail()
describe = iris.describe()
mean = iris.mean()

# print to screen, summary of stastics for initial observations. Describe function is very useful in this regard.  
print ("the first ten lines of the iris data set are:", head)
print ("the last ten lines of the iris data set are:", tail)
print ("a description of the iris data set:", describe)
print ("The mean of the iris data set is:", mean)

# Second output required for project- A histogram of the output of the variables 
iris.hist()

plt.show()
plt.close()

# Third output required for project- A scatter plot of the output of the variables 
sns.set_style("darkgrid")
sns.pairplot(iris, hue="species", height=4) #hue distinguished by species
plt.show()


# references:
# 1. Python Pandas read_csv – Load Data from CSV Files, https://www.shanelynn.ie/python-pandas-read_csv-load-data-from-csv-files/
# 2. Data Science with Python: Intro to Loading, Subsetting, and Filtering Data with pandas https://towardsdatascience.com/data-science-with-python-intro-to-loading-and-subsetting-data-with-pandas-9f26895ddd7f
# 3. Aggregations, Min, Max, and Everything In Between,https://jakevdp.github.io/PythonDataScienceHandbook/02.04-computation-on-arrays-aggregates.html
# 4. Box plot and Histogram exploration on Iris data, https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/.
# 5. Matplotlib Histogram, https://pythonspot.com/matplotlib-histogram/
# 6. seaborn.scatterplot, https://seaborn.pydata.org/generated/seaborn.scatterplot.html