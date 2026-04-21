# Program to perform arithmetic operations

# Taking input from user
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# Arithmetic operations
addition = a + b
subtraction = a - b
multiplication = a * b

# Handle division safely
if b != 0:
    division = a / b
    modulus = a % b
else:
    division = "Undefined (division by zero)"
    modulus = "Undefined (modulus by zero)"

# Display results
print("\nResults:")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Modulus:", modulus)