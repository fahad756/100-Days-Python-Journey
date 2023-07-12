# String

# Assign a string to the variable 'Name'
Name = "Fahad"

# Print each character of the string using a loop
for character in Name:
    print(character)

# String Slicing
names = "Fahad,Waseem,"

# Print a substring from index 0 to 4 (excluding index 5)
print(names[0:5])

# Print a substring from index 1 to 4 (excluding index 5)
print(names[1:5])

# Print a substring from the start to index 4 (excluding index 5)
print(names[:5])

# Print the complete string
print(names[:])

# Negative slicing: Print a substring from index 0 to -12 (excluding the last 12 characters)
print(names[0:-12])

# Negative slicing: Print a substring from index -3 to -1 (excluding the last character)
print(names[-3:-1])

# Length of string
name = "Fahad Waseem"

# Calculate and print the length of the string using the 'len()' function
print(len(name))
first = len(name)

# .
# .
# .
# Quick Quiz... What will it print?
nm = "Harry"
print(nm[-4:-2])
