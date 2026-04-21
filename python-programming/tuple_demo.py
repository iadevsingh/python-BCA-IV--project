# Program to demonstrate tuple operations and immutability

# Creating a tuple
t = (10, 20, 30, 40, 50)

print("Original tuple:", t)

# ------------------ TUPLE OPERATIONS ------------------

# Accessing elements
print("\nFirst element:", t[0])
print("Last element:", t[-1])

# Slicing
print("Sliced tuple (1 to 3):", t[1:4])

# Length
print("Length of tuple:", len(t))

# Count and index
print("Count of 20:", t.count(20))
print("Index of 30:", t.index(30))

# ------------------ IMMUTABILITY ------------------

print("\nDemonstrating immutability:")

try:
    t[0] = 100   # This will cause an error
except TypeError as e:
    print("Error:", e)

# ------------------ WORKAROUND ------------------

# Convert tuple to list, modify, then convert back
temp = list(t)
temp[0] = 100
t = tuple(temp)

print("\nAfter modification using list conversion:", t)