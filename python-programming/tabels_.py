# Program to print multiplication table

# Taking input from user
num = int(input("Enter a number: "))

print("\nMultiplication Table of", num)

# Using for loop
for i in range(1, 11):
    print(num, "x", i, "=", num * i)