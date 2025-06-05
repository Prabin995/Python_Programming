#Creating 1D and 2D Arrays
import numpy as np

arr_1d=np.array([10,20,30,40,50])
print("1D Array:\n ",arr_1d)

# 2D Array (Like a matrix)
arr_2d=np.array([[1,2,3],[4,5,6]])
print("2D Array:\n",arr_2d)

#np.linspace(start, stop, num)
lin_arr=np.linspace(0, 1, 5)
print("Linespace Array:\n",lin_arr)

#np.arange(start, stop, step)
#Creates an array with values from start to stop-1 with a step.
arange_arr = np.arange(0,10,2)
print("Arange Array:\n",arange_arr )

#Changes the shape of an existing array.
arr = np.arange(6) #[0, 1, 2, 3, 4, 5]
reshaped_arr = arr.reshape(2,3)
print("Reshaped to 2X3:\n",reshaped_arr)

#Useful for generating random numbers (used in ML for sampling, initializing weights, etc.)
rand_arr = arr.reshape(2,3) #Random float values between 0 and 1
print("Reshaped to 2X3:\n",rand_arr)