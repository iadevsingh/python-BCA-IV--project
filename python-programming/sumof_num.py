# Program to compute sum of first N natural numbers using while loop

# Taking input
n = int(input("Enter N: "))

# Initialize variables
i = 1
total = 0

# While loop
while i <= n:
    total += i
    i += 1

# Output
print("Sum of first", n, "natural numbers is:", total)