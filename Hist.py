# Richard Deegan
# Import Libraries 
import pandas as pd
import matplotlib.pyplot as plt

# Read Iris CSV file to into DataFrame and create Iris variable
iris = pd.read_csv("iris.csv")

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

# References

# Data science, Startups, Analytics, and Data visualisation, https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/
# Matplotlib Tutorial 5 - Histograms,https://www.youtube.com/watch?v=r75BPh1uk38
# Intro to Data Analysis / Visualization with Python, Matplotlib and Pandas | Matplotlib Tutorial, https://www.youtube.com/watch?v=a9UrKTVEeZA&t=747s
