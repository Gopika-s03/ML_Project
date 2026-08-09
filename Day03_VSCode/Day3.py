import numpy as np

# Create a NumPy array
arr = np.array([10, 20, 30, 40, 50])

print("Original Array:", arr)

# Indexing
print("First Element:", arr[0])
print("Last Element:", arr[-1])

# Slicing
print("Elements from index 1 to 3:", arr[1:4])

# Mathematical Operations
print("Addition (+5):", arr + 5)
print("Subtraction (-5):", arr - 5)
print("Multiplication (*2):", arr * 2)
print("Division (/2):", arr / 2)
print("Square:", arr ** 2)

# Statistical Functions
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# Reshape into 2D array
matrix = arr.reshape(5, 1)
print("\nReshaped Array (5x1):")
print(matrix)

# Create another array
arr2 = np.array([1, 2, 3, 4, 5])

# Array-based Calculations
print("\nSecond Array:", arr2)
print("Array Addition:", arr + arr2)
print("Array Multiplication:", arr * arr2)

# 2D Array
matrix2 = np.array([[1, 2], [3, 4]])
print("\n2D Array:")
print(matrix2)

# Transpose
print("Transpose of 2D Array:")
print(matrix2.T)
