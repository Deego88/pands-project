#Ricahrd Deegan

# Ask user for input of three variables.
x = float(input("Please enter sepal_lenght: "))
y = float(input("Please enter petal_lenght: "))
z = float(input("Please enter petal_width: "))


#Isolate Setosa measurements first taking rounded median values from describe() iris dat.
#Isolate Virsicolor measurements second, else veriginica as observed in scatter plot.   
if x <= float(5) and y <= float(4) and z <= float(4):
    print("species is setosa") 
elif x >= float(4) and y >= float(4) and z >= float(1):
    print("species is likely virsicolor")
else:
    print("species is likely veriginica")
