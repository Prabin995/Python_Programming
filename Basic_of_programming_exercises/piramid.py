#Making the programme to make primade by using multiple numbers 
rows = int(input("Enter the numbers of rows:  "))
for i in range (1, rows+1):
    print(" "*(rows-i), end=" ")
    for j in range (1, i+1):
        print(j, end=" ")
    print()