#Loops help you repeat tasks without writing code again and again
#for loop
for i in range(5):
    print(i)

#while loop
count = 0
while count<5:
    print(count)
    count +=1

#Lists in Python
#A list stores multiple items in a single variable.
numbers = [4, 7, 2, 9]
print(numbers[0])
print(len(numbers))

for num in numbers:
    print(num)

#Write a program to:
#Ask the user how many numbers they want to enter.
#Store those numbers in a list.
#Use a loop to find the total sum.
#Print the list and the sum.

Wanted_number = int(input("How many number do you want to enter?  "))
num_list = []
for i in range(Wanted_number):
    num = int(input(f" Enter number {i+1}:  "))
    num_list.append(num)

total = sum(num_list)
print("List:",num_list)
print("sum:",total)