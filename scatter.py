# Third output required for project- A scatter plot of the output of the variables 
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# First output required for project- Read iris CSV file to into DataFrame
iris = pd.read_csv("iris.csv")

sns.set_style("darkgrid")
sns.pairplot(iris, hue="species", height=4) #hue distinguished by species
plt.show()
