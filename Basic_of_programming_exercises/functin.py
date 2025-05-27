#What is a function?
#A function is a reusable block of code that does something. You define it once and use it many times.
 

def greet(name):
    print("Hello",name)

greet("Prabin")
greet("World")


#Let's write a function that checks even or odd:
def check_even_odd(number):
    if number % 2==0:
        return "Even"
    else:
        return "Odd"
    
#testing the function 
num = int(input("Enter a number:  "))
result = check_even_odd(num)
print(f"{num} is {result}")


# Write a function called is_positive_negative_zero(number) that:
#Returns "Positive" if the number is greater than 0
#Returns "Negative" if the number is less than 0
#Returns "Zero" if the number is 0

def is_positive_negative_zero(number):
    if number>0:
        return "Positive number!"
    elif number ==0:
        return "Zero!"
    else:
        return "Negative number!"
    
num = int(input("Enter a number:    "))
result = is_positive_negative_zero(num)
print(f"{num} is {result}")
