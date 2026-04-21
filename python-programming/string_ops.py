# Program to demonstrate string operations

# Taking input
text = input("Enter a string: ")

# Slicing
print("\nSlicing:")
print("First 3 characters:", text[:3])
print("Last 3 characters:", text[-3:])
print("Middle part:", text[1:-1])

# Concatenation
extra = input("\nEnter another string to concatenate: ")
result = text + " " + extra
print("Concatenated string:", result)

# Reversing
reverse = text[::-1]
print("\nReversed string:", reverse)