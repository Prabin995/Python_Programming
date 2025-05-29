#Ask how many numbers the user wants to enter.
#Store them in a list.
#Use a loop and logic to count:
#how many are even
#how many are odd
#Print the result.


count=int(input("How many numbers do you want to enter?  "))
numbers = []
even_count = 0
odd_count = 0
for i in range(count):
    num = int(input(f"Enter number {i+1}:  "))
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count +=1

print("Even Numbers:  ", even_count)
print("Odd Numbers:  ", odd_count)
