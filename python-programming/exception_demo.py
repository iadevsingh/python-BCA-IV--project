# Program to demonstrate exception handling

try:
    # Taking input
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    # Division operation
    result = a / b

    print("Result:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")

except ValueError:
    print("Error: Please enter valid integers!")

except Exception as e:
    print("Some unexpected error occurred:", e)

finally:
    print("Program execution completed.")
    