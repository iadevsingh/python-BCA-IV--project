# Program to count frequency of characters

# Taking input
text = input("Enter a string: ")

# Create empty dictionary
freq = {}

# Count frequency
for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

# Display result
print("\nCharacter Frequencies:")
for key, value in freq.items():
    print(key, ":", value)