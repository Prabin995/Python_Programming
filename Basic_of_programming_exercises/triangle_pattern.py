#for making triangle of numbers 
rows = int(input("Enter the number of rows:  "))
for i in range (1, rows +1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()


#reversing this triangle.
rows1 = int(input("Enter the number of rows:  "))
for i in range (rows1, 0, -1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()