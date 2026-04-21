# Program to write and append data to a file

# -------- Writing to a file (overwrites if file exists) --------
with open("sample.txt", "w") as file:
    file.write("Hello, this is the first line.\n")
    file.write("This file is created using write mode.\n")

print("Data written successfully.")

# -------- Appending to the same file --------
with open("sample.txt", "a") as file:
    file.write("This line is added later using append mode.\n")
    file.write("Appending does not delete previous data.\n")

print("Data appended successfully.")