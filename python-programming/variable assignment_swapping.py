# Demonstrating variable assignment and swapping

# Variable assignment
a = 10
b = 20

print("Before swapping:")
print("a =", a)
print("b =", b)

# Method 1: Swapping using a temporary variable
temp = a
a = b
b = temp

print("\nAfter swapping (using temporary variable):")
print("a =", a)
print("b =", b)

# Reassign values again for second method
a = 10
b = 20

# Method 2: Swapping without using a temporary variable
a, b = b, a

print("\nAfter swapping (without temporary variable):")
print("a =", a)
print("b =", b)