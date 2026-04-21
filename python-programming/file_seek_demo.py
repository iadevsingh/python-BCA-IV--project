# Program to demonstrate file pointer using seek()

# Create a sample file
with open("sample.txt", "w") as f:
    f.write("Hello Python\nWelcome to File Handling\nSeek function demo")

# Open file in read mode
with open("sample.txt", "r") as f:
    
    # Read first 5 characters
    print("Reading first 5 characters:")
    print(f.read(5))
    
    # Move pointer to beginning
    f.seek(0)
    print("\nAfter seek(0), reading again:")
    print(f.read(5))
    
    # Move pointer to 6th position
    f.seek(6)
    print("\nAfter seek(6), reading next 10 characters:")
    print(f.read(10))
    
    # Move pointer to end
    f.seek(0, 2)   # 2 means end of file
    print("\nPointer moved to end of file.")
    print("Current position:", f.tell())