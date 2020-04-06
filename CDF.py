#Richard Deegan

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

iris = pd.read_csv("iris.csv")

setosa = iris[iris["species"] == "setosa"]
versicolor = iris[iris["species"] == "versicolor"]
virginica = iris[iris["species"] == "virginica"]

#distribution plot for species SL,PW and PL. 
sns.FacetGrid(iris, hue="species", height=5,) \
    .map(sns.distplot, "sepal_length") \
    .add_legend() 

sns.FacetGrid(iris, hue="species", height=5,) \
    .map(sns.distplot, "petal_width") \
    .add_legend() 

sns.FacetGrid(iris, hue="species", height=5,) \
    .map(sns.distplot, "petal_length") \
    .add_legend() 

plt.show()
plt.figure(figsize=(15,10))



#References 
#Exploratory Data Analysis:Uni - variate analysis of Irish data set, https://medium.com/analytics-vidhya/exploratory-data-analysis-uni-variate-analysis-of-iris-data-set-690c87a5cd40


