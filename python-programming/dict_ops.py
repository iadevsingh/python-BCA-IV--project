# Program to demonstrate dictionary operations

# Creating a dictionary
student = {
    "name": "Dev",
    "age": 20,
    "course": "BCA"
}

print("Original dictionary:", student)

# ------------------ ADD ------------------
# Adding a new key-value pair
student["marks"] = 85
print("\nAfter adding (marks):", student)

# ------------------ UPDATE ------------------
# Updating existing value
student["age"] = 21
print("After updating age:", student)

# ------------------ DELETE ------------------

# Using del
del student["course"]
print("After deleting 'course' using del:", student)

# Using pop()
removed = student.pop("marks")
print("After pop('marks'):", student)
print("Removed value:", removed)