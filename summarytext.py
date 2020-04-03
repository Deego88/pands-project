# Richard Deegan
# import pands and create iris variable
import pandas as pd

iris = pd.read_csv("iris.csv")
# create new text document and append the description of the iris data set 
with open("summary.txt", "a") as f:
    f.write(iris.describe().to_string())
# appened string text to the end of the text document
with open ("summary.txt", "a") as f:
    f.write("    This is a summary of the variables in a single text file")

