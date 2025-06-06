import numpy as np
a = np.array([1,2,3])
b = np.array([4,5,6])

print("Addition: ", a+b)
print("Subtraction: ", a-b )
print("Multiplication: ", a*b)
print("Division:", b/a )

# Array Slicing & Indexing (1D & 2D)
arr = np.array([10, 20, 30, 40, 50])
print(arr[0])  #First element
print(arr[1:4]) #Slice from index 1 to 3
print(arr[-1])  # Last element

#2D Slicing 
arr2d = np.array([1, 2, 3],[4, 5, 6])
print(arr2d[0])  #First row 
print(arr2d[1,2])  #Element at 2nd row, 3rd column 
print(arr2d[:,1])  #All rows, 2nd column

#Extract all even numbers from an array using boolean indexing:
arr = np.array([1, 4, 6, 7, 9, 12])
even = arr[arr % 2 == 0]
