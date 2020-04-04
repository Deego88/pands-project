# Richard Deegan
# Import Libraries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# First output required for project- Read iris CSV file to into DataFrame
iris = pd.read_csv("iris.csv")

# create new text document and append the description of the iris data set 
with open("summary.txt", "a") as f:
    f.write(iris.describe().to_string())
# appened string text to the end of the text document
with open ("summary.txt", "a") as f:
    f.write("    This is a summary of the variables in a single text file")

# create variables and print to screen, initial look at data set. 
head = iris.head()
tail = iris.tail()
describe = iris.describe()
mean = iris.mean()

# print to screen, summary of stastics for initial observations. Describe function is very useful in this regard.  
print (head)
print (tail)
print (describe)
print (mean)

# Second output required for project- A histogram of the output of the all variables 
iris.hist()

plt.show()
plt.close()


# Create 3 species variables that Use Boolean logic to select relevant species row and column data
setosa = iris.loc[iris["species"] == "setosa"]
versicolor = iris.loc[iris["species"] == "versicolor"]
virginica = iris.loc[iris["species"] == "virginica"]

# look at each species type under the four variables
# Setosa variables
setosa1 = setosa.sepal_length
plt.hist(setosa1)
plt.xlabel("Measurements in CM")
plt.ylabel("Frequency of Occurrence")
plt.title("Setosa Sepal Length")

plt.savefig("Setosa Sepal Length.png", dpi=72,)
plt.show()

setosa2 = setosa.sepal_width
plt.hist(setosa2)
plt.xlabel("Measurements in CM")
plt.ylabel("Frequency of Occurrence")
plt.title("Setosa Sepal Width")

plt.savefig("Setosa Sepal Width.png", dpi=72,)
plt.show()

setosa3 = setosa.petal_length
plt.hist(setosa3)
plt.xlabel("Measurements in CM")
plt.ylabel("Frequency of Occurrence")
plt.title("Setosa Petal Length")

plt.savefig("Setosa Sepal Length.png", dpi=72,)
plt.show()

setosa4 = setosa.petal_width
plt.hist(setosa4)
plt.xlabel("Measurements in CM")
plt.ylabel("Frequency of Occurrence")
plt.title("Setosa Petal Width")

plt.savefig("Setosa Sepal Width.png", dpi=72,)
plt.show()

# Versicolor variables
versicolor1 = versicolor.sepal_length
plt.hist(versicolor1)
plt.xlabel("Measurements in CM")
plt.ylabel("Frequency of Occurrence")
plt.title("Versicolor Sepal Length")

plt.savefig("Versicolor Sepal Length.png", dpi=72,)
plt.show()

versicolor2 = versicolor.sepal_width
plt.hist(versicolor2)
plt.xlabel("Measurements in CM")
plt.ylabel("Frequency of Occurrence")
plt.title("Versicolor Sepal Width")

plt.savefig("Versicolor Sepal Width.png", dpi=72,)
plt.show()

versicolor3 = versicolor.petal_length
plt.hist(versicolor3)
plt.xlabel("Measurements in CM")
plt.ylabel("Frequency of Occurrence")
plt.title("Versicolor Petal Length")

plt.savefig("Versicolor Petal Length.png", dpi=72,)
plt.show()

versicolor4 = versicolor.petal_width
plt.hist(versicolor4)
plt.xlabel("Measurements in CM")
plt.ylabel("Frequency of Occurrence")
plt.title("Versicolor Petal Width")

plt.savefig("Versicolor Petal Width.png", dpi=72,)
plt.show()

# Virginica variables
virginica1 = virginica.sepal_length
plt.hist(virginica1)
plt.xlabel("Measurements in CM")
plt.ylabel("Frequency of Occurrence")
plt.title("Virginica Sepal Length")

plt.savefig("Virginica Sepal Length.png", dpi=72,)
plt.show()

virginica2 = virginica.sepal_width
plt.hist(virginica2)
plt.xlabel("Measurements in CM")
plt.ylabel("Frequency of Occurrence")
plt.title("Virginica Sepal Width")

plt.savefig("Virginica Sepal Width.png", dpi=72,)
plt.show()

virginica3 = virginica.petal_length
plt.hist(virginica3)
plt.xlabel("Measurements in CM")
plt.ylabel("Frequency of Occurrence")
plt.title("Virginica Petal Length")

plt.savefig("Virginica Petal Length.png", dpi=72,)
plt.show()

virginica4 = virginica.petal_width
plt.hist(virginica4)
plt.xlabel("Measurements in CM")
plt.ylabel("Frequency of Occurrence")
plt.title("Virginica Petal Width")

plt.savefig("Virginica Petal Width.png", dpi=72,)
plt.show()

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
# 7. Data science, Startups, Analytics, and Data visualisation, https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/
# 8. Matplotlib Tutorial 5 - Histograms,https://www.youtube.com/watch?v=r75BPh1uk38
# 9. Intro to Data Analysis / Visualization with Python, Matplotlib and Pandas | Matplotlib Tutorial, https://www.youtube.com/watch?v=a9UrKTVEeZA&t=747s
