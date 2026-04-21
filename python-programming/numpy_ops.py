import numpy as np

# ------------------ ARRAY CREATION ------------------
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20, 30, 40, 50])

print("Array 1:", arr1)
print("Array 2:", arr2)

# ------------------ INDEXING ------------------
print("\nIndexing:")
print("First element of arr1:", arr1[0])
print("Last element of arr1:", arr1[-1])
print("Slice (1 to 3):", arr1[1:4])

# ------------------ ARITHMETIC OPERATIONS ------------------
print("\nArithmetic Operations:")
print("Addition:", arr1 + arr2)
print("Subtraction:", arr2 - arr1)
print("Multiplication:", arr1 * arr2)
print("Division:", arr2 / arr1)