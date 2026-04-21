# Custom Exception class
class NegativeNumberError(Exception):
    pass

try:
    # Taking input
    num = int(input("Enter a positive number: "))

    # Raise custom exception if number is negative
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")

    # Normal operation
    print("You entered:", num)

except NegativeNumberError as e:
    print("Custom Exception:", e)

except ValueError:
    print("Error: Please enter a valid integer!")

finally:
    print("This block always executes (cleanup / end message).")