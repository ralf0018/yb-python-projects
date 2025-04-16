import numpy as np

# Create a numpy array of the first 10 positive integers
arr = np.arange(1,11)

# print the array
print(arr)

# print array shape and data type
print(f"array shape: {arr.shape}")
print(f"array data type: {arr.dtype}")

# Multiply each element by 2 and print the result
newarr = arr*2
print(newarr)