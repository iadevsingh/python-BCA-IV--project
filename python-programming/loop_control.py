# Demonstrating break, continue, and pass

# 1. Using break
print("Using break:")
for i in range(1, 11):
    if i == 6:
        break   # stops the loop when i = 6
    print(i)

# 2. Using continue
print("\nUsing continue:")
for i in range(1, 11):
    if i == 6:
        continue   # skips 6 and continues loop
    print(i)

# 3. Using pass
print("\nUsing pass:")
for i in range(1, 6):
    if i == 3:
        pass   # does nothing, acts as placeholder
    print(i)