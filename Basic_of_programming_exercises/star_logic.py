#Write a program that prints this triangle of stars (*) based on user input:
#If the user enters 5, it should print:
row = int(input("Enter the number of row:  "))
for i in range (1, row+1):
    print("*"*i)
 
#Print this pattern when the user enters 5:
rows = int(input("Enter the numbers of rows:  "))
for i in range(rows,0, -1):
    print("*"*i)
