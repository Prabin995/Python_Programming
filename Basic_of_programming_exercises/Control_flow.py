#if, elif, else lets your program make decisions:
age= int(input("Please type your Age    "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are Not adult.")


#if we want to find out grade base distrubutin:(For loop example)
Score = 85
if Score >= 90:
    print("Grade A!")
elif Score >= 75:
    print("Grade B!")

else:
    print("Grade C or below!")


#Loops repeat actions 
for i in range (5):
    print("Number:" , i)



#While loop example 

count = 0
while count<5:
    print("Count is", count)
    count +=1
    