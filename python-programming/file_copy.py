# Program to copy contents of one file to another

# Open source file in read mode
with open("source.txt", "r") as src:
    data = src.read()

# Open destination file in write mode
with open("destination.txt", "w") as dest:
    dest.write(data)

print("File copied successfully!")