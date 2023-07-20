# TUPLE

# Create a tuple named 'tup' with a mix of integers and strings.
tup = (1, 5, 2, "Day", 65, 7)

# Print the type of 'tup' and its contents.
print(type(tup), tup)

# Find and print the length of the tuple.
print(len(tup))

# Access and print the first element of the tuple.
print(tup[0])

# Slice the tuple from index 1 to index 2 (exclusive) and print the result.
print(tup[1:3])

# Create another tuple 'tup1' with three integers.
tup1 = (2, 3, 4)

# Concatenate 'tup' and 'tup1' into a new tuple 'fin' and print the result.
fin = tup + tup1
print(fin)

# Convert 'names' tuple to a list 'temp'.
names = ("Fahad", "Waseem", "Ali", "Usman", "Hamza")
temp = list(names)

# Add "Josh" to the end of the list, then remove the first element ("Fahad").
temp.append("Josh")
temp.pop(0)

# Convert 'temp' list back to a tuple 'names'.
names = tuple(temp)
print(names)

# Create a tuple 'numbers' with multiple occurrences of the value 8.
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 98, 8, 8, 8)

# Count and print the number of occurrences of the value 8 in 'numbers'.
print(numbers.count(8))
