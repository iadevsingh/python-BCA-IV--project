# Program to demonstrate list slicing and manipulation

# Creating a list
numbers = [10, 20, 30, 40, 50, 60]

print("Original list:", numbers)

# ------------------ SLICING ------------------
print("\nList Slicing:")
print("First 3 elements:", numbers[:3])
print("Last 3 elements:", numbers[-3:])
print("Middle elements:", numbers[1:5])
print("Reversed list:", numbers[::-1])

# ------------------ MANIPULATION ------------------
print("\nList Manipulation:")

# Append
numbers.append(70)
print("After append(70):", numbers)

# Insert
numbers.insert(2, 25)
print("After insert(2, 25):", numbers)

# Remove
numbers.remove(40)
print("After remove(40):", numbers)

# Pop
numbers.pop()
print("After pop():", numbers)

# Update value
numbers[0] = 5
print("After updating first element:", numbers)

# Sort
numbers.sort()
print("After sort():", numbers)