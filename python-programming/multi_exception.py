# Program to demonstrate multiple exception handling

try:
    # Taking inputs
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    # List for demonstration
    nums = [10, 20, 30]

    # Operations
    print("Division result:", a / b)          # May cause ZeroDivisionError
    print("List element:", nums[5])           # May cause IndexError

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

except ValueError:
    print("Error: Invalid input! Please enter numbers only.")

except IndexError:
    print("Error: List index out of range!")

except Exception as e:
    print("Unexpected error:", e)

finally:
    print("Program finished.")