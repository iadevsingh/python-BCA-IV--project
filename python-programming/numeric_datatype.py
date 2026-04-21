a = 10        # int
b = 5.5       # float

# Display values and their types
print("Integer value (a):", a, "Type:", type(a))
print("Float value (b):", b, "Type:", type(b))

# Implicit type conversion (int -> float)
sum_result = a + b
print("\nAfter implicit conversion (a + b):", sum_result, "Type:", type(sum_result))

# Explicit type conversion (float -> int)
converted = int(b)
print("After explicit conversion (float to int):", converted, "Type:", type(converted))

# Explicit conversion in division
division = float(a) / 3
print("\nExplicit conversion in division (a/3):", division, "Type:", type(division))