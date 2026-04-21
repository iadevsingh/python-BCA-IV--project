# Functions for string operations
def string_operations(text):
    print("\n--- String Operations ---")
    print("Original string:", text)
    print("Uppercase:", text.upper())
    print("Lowercase:", text.lower())
    print("Reversed:", text[::-1])
    print("Length:", len(text))


# Functions for list operations
def list_operations(lst):
    print("\n--- List Operations ---")
    print("Original list:", lst)
    print("Length:", len(lst))
    print("Maximum:", max(lst))
    print("Minimum:", min(lst))
    print("Sum:", sum(lst))
    
    lst.append(100)
    print("After append(100):", lst)


# Main program
# String input
text = input("Enter a string: ")
string_operations(text)

# List input
lst = list(map(int, input("\nEnter list elements separated by space: ").split()))
list_operations(lst)