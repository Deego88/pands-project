# Programming and Scripting Project 2020, Iris Data Set

# G00387896 Richard Deegan

## Table of Contents

## [Introduction/Background](https://github.com/Deego88/pands-project/blob/master/README.md#introduction-1)

## [Problem Statement](https://github.com/Deego88/pands-project/blob/master/README.md#problemstatement) 

## [User Guide](https://github.com/Deego88/pands-project/blob/master/README.md#user-guide) 

## [Program Code Explained](https://github.com/Deego88/pands-project#program-code-explained)

## [Libraries](https://github.com/Deego88/pands-project/blob/master/README.md#libraries-1)

## [Results](https://github.com/Deego88/pands-project/blob/master/README.md#results-1)
  
## [Summary and Conclusion of Data Set](https://github.com/Deego88/pands-project/blob/master/README.md#summary-and-conclusion-of-data-set-1)
  
## [References](https://github.com/Deego88/pands-project/blob/master/README.md#references-1)
  
  
## Introduction/Background
  
The purpose of this project is to conduct an exploratory data analysis of the Iris data set. This project forms part of the Programing and Scripting module assessment for GMITs Data Analytics higher Diploma course. The full set of project deliverables, instructions and grading criteria can be found [here.](https://github.com/Deego88/pands-project/blob/master/Pands%20Project.pdf)

The iris dataset was first introduced by Ronald Fisher in 1936 in his paper "The Use of Multiple Measurements in Taxonomic Problems". 
Ronald Fisher was a British statistician who made impressive strides in the field of modern statistical science.  The Iris data set is well known throughout the world of statistics and is commonly utilised for exploratory data analysis. The Iris  data set is sometimes referred to as the Anderson’s Iris data set, simply because Edgar Anderson was the individual who collected the data on the Iris flowers which was subsequently used. 

![](https://github.com/Deego88/pands-project/blob/master/03_iris.png)

Essentially the Iris data set contains the following data:

The data set contains the following:

•	Three types of Species: 
1. The Iris Setosa.
2. The Iris Versicolor. 
3. The Iris Virginic.

•	Four measurements of each species:

1. Sepal length.
2. Sepal width.
3. Petal length. 
4. Petal width.

•	Fifty samples of Iris flower from each species (150 total). 

The flowers are measured in centimetres of four columns, the fifth column details the species type. The data for the Iris data set is extracted from a CSV, this data set is plentiful and readily available on multiple sources on the internet. For example, the raw CSV Irish data set can be found [here](https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/639388c2cbc2120a14dcf466e85730eb8be498bb/iris.csv
). 

 ## Problem Statement
 
This project will conduct an analysis of the Iris data set. As part of this analysis the project will utilise python code. Detailed explanations of the python code for the user will be provided; specifically, on the journey of analysing a data set with Python. This project will create a program that:

  - outputs a summary of each variable to a single text file,
  
  - saves a histogram of each variable to png files, and
  
  - outputs a scatter plot of each pair of variables.

## User Guide 
This section will explain everything the user requires to know about downloading and using the files contained in the repository.

### How to Download
In order to download all the flies to a zip folder; navigate to relevant GitHub repository at:  
https://github.com/Deego88/pands-project
1.	Click on the green “clone or download” button on the right side of your screen.
2.	Click on “download ZIP” and save the ZIP to the desired location on your computer. 
3.	Move to the ZIP files location and extract the compressed (.zip) file to your computer. 

### Running the Program 
This program has been written by Python 3.7.1 and consequently the user will require a version of Python not later than Python 3.7. It is recommended that the user download the Anaconda distribution of Python 3.7, and to ensure that only official verified copies are downloaded. Furthermore, this program requires certain libraries to be installed on Python which are explained later. Once the ZIP has been downloaded and extracted the user can run the program. In order to run the program from the command line:

1.	Run the command line prompt, (commander is recommended)
2.	Use the change directory (cd) command to navigate to the correct folder 
3.	Run the program by typing **python ProgramsNameHere.py**

The python program analysis.py does the following:
1.	Reads in the Iris data set CSV file for analysis.
2.	Outputs a summary of each variable in the Iris data set to a text file called summary.txt.
3.	Saves an individual Histogram of each variable to png files.
4.	Produces a scatter pair plot for each variable. 


### Libraries

 The following Python libraries are used to conduct the data analysis of the Iris data set:
 
 1. pandas- pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool.
 2. numpy- provides a high-performance multidimensional array object, and tools for working with these arrays.
 3. matplotlib- is a plotting library and allows for the production of graphs, plots and charts. 
 4. seaborn- is a Python data visualisation library based on matplotlib, it provides a high-level interface for graphics.
 
 
 ## Program Code Explained 
  
 Three separate python codes were coded to form the analysis.py program, they are explained as follows:
 
1.	The program “summary.py” was coded up to achieve the first project deliverable of creating an output a summary of each variable to a single text file. 
First the code opened the summary.txt file with the “a” append function. F.write was used to append the description of the Irish data set to the summary.txt file, by utilising the describe () function.  Finally, the string text was appended to the end of the summary.txt file.

![](https://github.com/Deego88/pands-project/blob/master/Images%20for%20README/Summary%20Output.PNG)

![](https://github.com/Deego88/pands-project/blob/master/Images%20for%20README/Describe%20Iris%20data.PNG)

2.	The program Hist.py was created coded to achieve the second deliverable fo the project of saving a histogram of each variable to png files.  
In order to create an individual histogram for each variable it was first necessary to separate the exact variables required. To select the relevant column and row to capture the correct data the .loc function was used. The variables setosa, versicolor and verginica were created which contained only their species rows of data. The data of each variable was then further narrowed by selecting only the specific measurement variable eg Sepal Length, Sepal Width etc. This was done by creating four new variables; setosa1, setosa2, setosa3 and setosa4 where each variable plotted a histogram for the four measurements contained in the Irish data set. This code was then copied and reapplied for the versicolor and virginica species. The plt.savefig() was used to save the histogram files to png files. 

![](https://github.com/Deego88/pands-project/blob/master/Images%20for%20README/Histogram%20code.PNG)

3.	Scatter.py was coded to achieved the third deliverable of the project to output a scatter plot of each pair of variables. The library seaborn was imported and used. Sns.pairpolt() function was used to pair off the variables in pairs. 

![](https://github.com/Deego88/pands-project/blob/master/Images%20for%20README/Scatter%20Pair%20Plot.PNG)

The program analysis.py was the main program created to house the other three programs. hist.py, summary.py and scatter.py were all copied and pasted into analysis.py to form one single piece of code that achieves all three project deliverables. Analysis.py was then ran as a single piece of code and minor adjustments were made. 


## Results

![Histogram Output](https://github.com/Deego88/pands-project/blob/master/Images%20for%20README/Iris%20Histogram%20Output.PNG)


![Scatter Pair Plot Output](https://github.com/Deego88/pands-project/blob/master/Images%20for%20README/Iris%20Scatter%20Pair%20Plot%20Output.png)

The seaborn plot "pairplot", shows the bivariate relation between each pair of features. Bivariate analysis can be helpful in testing the simple hypotheses of association between variables.

## Summary and Conclusion of Data Set

In summary, the Iris data set contains three species of flower; Setosa, Versicolor and Virginica. Also contained in this data set are four variable measurements; Petal length and width, Sepal length and width. Each species of flower tends to conform to certain parameters within the measurements. It is therefore possible to predict which specie type a flower is based on the measurements. For example, if a species has short sepal (4.4 – 5.8cm), short petals (1.2 - 4.4cm) and narrow petals (0.1 - 4.4cm) it is most likely a Setosa, if a species has a long sepal approx. (4.4 - 7.9cm), long petals (4.4 - 6.9cm), and wide petals (1.3- 2.5cm) it is most likely a Virginica. Consequently, any species that resides between these two is most likely to be a Versicolor. 
Note: long is median to max values and short median to min values. 

From this data analysis we can make various observations. For example, if we consider the petal length, we can see that it has a large standard deviation (1.74) in data and a large variance (3.03), a large variance in data points gives rise to a highly defined graph with little overlap and a clear distribution. Furthermore, if we consider the sepal width standard deviation of (0.42) and the variance of (0.17) it would explain why the sepal width graph overlaps and displays clustered points close to the mean with little variance. Therefore, sepal width is not a desirable measurement to consider when trying to categorise the species into their types based off the data measurements.  


## References
 
1. UCI Machine Learning Repository – Iris Data Set, http://archive.ics.uci.edu/ml/datasets/Iris
2. Iris Data Set, https://www.ritchieng.com/machine-learning-iris-dataset/
3. Basic Analysis of the Iris Data set Using Python, https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342
4. Statistical Analysis of the Iris Flower Dataset, http://patrickhoey.com/downloads/Computer_Science/03_Patrick_Hoey_Data_Visualization_Dataset_paper.pdf
4. Ronald Fischer, https://en.wikipedia.org/wiki/Ronald_Fisher
5. Data science, Startups, Analytics, and Data visualisation, https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/
6. Matplotlib Tutorial Histograms,https://www.youtube.com/watch?v=r75BPh1uk38
7. Intro to Data Analysis / Visualization with Python, Matplotlib and Pandas | Matplotlib Tutorial, https://www.youtube.com/watch?v=a9UrKTVEeZA&t=747s
8 Python Pandas read_csv – Load Data from CSV Files, https://www.shanelynn.ie/python-pandas-read_csv-load-data-from-csv-files/
9. Data Science with Python: Intro to Loading, Subsetting, and Filtering Data with pandas https://towardsdatascience.com/data-science-with-python-intro-to-loading-and-subsetting-data-with-pandas-9f26895ddd7f
10. Aggregations, Min, Max, and Everything In Between,https://jakevdp.github.io/PythonDataScienceHandbook/02.04-computation-on-arrays-aggregates.html
11. Box plot and Histogram exploration on Iris data, https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/.
12. Matplotlib Histogram, https://pythonspot.com/matplotlib-histogram/
13. Seaborn.scatterplot, https://seaborn.pydata.org/generated/seaborn.scatterplot.html





