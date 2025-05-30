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
    