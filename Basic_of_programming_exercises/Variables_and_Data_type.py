#Python variables can hold different types of data. Here are some examples:

#integer 
age = 24

#Floate (decimal)
height=5.9

#String (text)
name = "Prabin"

#Boolen (true/false)
is_student= True 

#we can check the type using:
print(type(age))
print(type(height))
print(type(name))
print(type(is_student))

#We need to use loop function if we want to print all once 
variables = [age, height, name, is_student]

for var in variables:
    print(type(var))
    