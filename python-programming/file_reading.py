# Program to demonstrate read(), readline(), and readlines()

# Open the file in read mode
file = open("sample.txt", "r")

# -------- Using read() --------
print("Using read():")
content = file.read()
print(content)

# Move file pointer to beginning
file.seek(0)

# -------- Using readline() --------
print("\nUsing readline():")
line1 = file.readline()
line2 = file.readline()
print("First line:", line1)
print("Second line:", line2)

# Move file pointer to beginning again
file.seek(0)

# -------- Using readlines() --------
print("\nUsing readlines():")
lines = file.readlines()
print(lines)

# Close the file
file.close()