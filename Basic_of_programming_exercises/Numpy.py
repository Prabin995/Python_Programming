import numpy as np
#Create a Numpy array
data = np.array([1,2,3,4,5])
#Element-wise operations
print("Original: ",data)
print("Added 5: ",data +5 )
print("Squared: ", data**2)

#Statistics
print("Mean: ",np.mean(data))
print("Max: ",np.max(data))
print("Sum: ", np.sum(data))