#Ricahrd Deegan

# Ask user for input of three variables.
x = float(input("Please enter petal_lenght: "))
y = float(input("Please enter petal_width: "))


#Isolate Setosa measurements first taking largets petal lenght value.
#Isolate Virsicolor measurements second, everything else is likely veriginica.   
if x <= float(1.9):
    print("species is setosa") 
elif x > float(1.9) and x <= float(4.8):
    print("species is likely virsicolor ")
else:
    print("species is likely virginica")

