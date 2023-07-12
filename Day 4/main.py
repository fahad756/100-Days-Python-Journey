# String Methods

# strings are immutable
a = "Fahad"
b = "FAHAD.................................."
names = "Fahad,Waseem,Asad,Umair,Ali"

# Print the value of 'b'
print(b)

# Convert 'a' to uppercase and print
print(a.upper())

# Convert 'a' to lowercase and print
print(a.lower())

# Remove trailing dots from 'b' and print
print(b.rstrip("."))

# Replace "FAHAD" with "Waseem" in 'b' and print
print(b.replace("FAHAD", "Waseem"))

# Split 'names' into a list of names separated by commas and print
print(names.split(","))

# Capitalize the first letter of 'log' and print
log = "this is a log"
print(log.capitalize())

# Center-align 'log' within a field of width 50 and print
print(log.center(50))

# Count the occurrences of the letter 'a' in 'names' and print
print(names.count("a"))

# Find the first occurrence of "Asad" in 'names' and print its index
print(names.find("Asad"))

# 'index' and 'find' are the same, but 'index' raises an error if not found
print(names.index("Asad"))

# Check if 'val' is alphabetic and print the result
val = "Hope"
print("Is alphabetic:", val.isalpha())

# Check if 'val' is numeric and print the result
print("Is numeric:", val.isnumeric())

# Check if 'val' is alphanumeric and print the result
print("Is alphanumeric:", val.isalnum())

# Check if 'val' is printable and print the result
print("Is printable:", val.isprintable())

# Check if 'val' consists of whitespace only and print the result
print("Is whitespace:", val.isspace())

# Check if 'val' is in title case and print the result
print("Is title case:", val.istitle())

# Swap the case of characters in 'val' and print
print(val.swapcase())

# Convert the first character of each word in 'log' to title case and print
print(log.title())
