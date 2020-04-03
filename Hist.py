# Richard Deegan
# Import Libraries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# First output required for project- Read iris CSV file to into DataFrame
iris = pd.read_csv("iris.csv")

setosa = iris.species.iloc[0:50]
#versicolor = iris.species.iloc[51:100]
#virginica = iris.species.iloc[100:150]
print (setosa)
#print (versicolor)
#print (virginica)

