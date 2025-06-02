#A while loop runs as long as the condition is True.
i =1
while i <= 5:
    print(i)
    i += 1

#Asks the user to input numbers
#Keeps asking until they enter 0
#Then prints the total sum of all numbers entered
num_list=[]
while True:
    number = int(input("Enter the number:  "))
    if number == 0:
        break
    num_list.append(number)
total = sum(num_list)
print("Numbers entered:", num_list)
print("Total sum:", total)

#Write a program that:
#Asks the user to enter 5 numbers
#If the number is negative, skip it using continue
#Add only positive numbers
#Print the list and the total sum

num_list1=[]
i=0
while i<5:
    number1=int(input("Enter the number:  "))
    if number1<0:
        continue
    num_list1.append(number1)
    i+=1
total1=sum(num_list1)
print("Numbers Entered:  ",num_list1)
print("total sum:",total1)
