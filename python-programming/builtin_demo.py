# Program to demonstrate built-in functions

# -------- LIST --------
numbers = [10, 20, 30, 40, 50]

print("List:", numbers)
print("Length of list:", len(numbers))
print("Maximum value:", max(numbers))
print("Minimum value:", min(numbers))
print("Sum of elements:", sum(numbers))

# -------- STRING --------
text = "Python Programming"

print("\nString:", text)
print("Length of string:", len(text))
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Count of 'o':", text.count('o'))
print("Replace 'Python' with 'Java':", text.replace("Python", "Java"))

# -------- DICTIONARY --------
student = {
    "name": "Dev",
    "age": 20,
    "marks": 85
}

print("\nDictionary:", student)
print("Length of dictionary:", len(student))
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())