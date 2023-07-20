#LIST
# Let's define a list named Randomv with a mix of integers and strings.
Randomv = [1, "Fahad", 4, 1, "4", "Home", 7]

# Example of slicing: This will print elements from index 0 to index 4 (exclusive) with a step of 2.
print(Randomv[0:5:2])

# Commented out the following code block as it is not necessary for the current output.
# for random in Randomv:
#     print(random)

# List comprehension is a concise way to create lists. Here we create a list from 0 to 3 (exclusive).
lst = [i for i in range(4)]
print(lst)

# List comprehension with arithmetic operation: This will create a list of values where each element is doubled.
lst = [i + i for i in range(5)]
print(lst)

# List comprehension with condition: This will create a list of squares of even numbers from 0 to 4.
even = [i*i for i in range(6) if i % 2 == 0]
print(even)

# List Manipulation
numbers = [4, 6, 3, 1, 5, 2]

# Append 7 to the end of the list.
numbers.append(7)
print(numbers)

# Sort the list in ascending order.
numbers.sort()
print(numbers)

# Find the index of the value 1 in the list.
print(numbers.index(1))

# Create a new list named 'lists' that references the same list as 'numbers'.
# Modifying 'lists' will also modify 'numbers' because they point to the same object.
lists = numbers
lists[0] = 9

# Insert 55 at index 1 in the 'numbers' list.
numbers.insert(1, 55)
print(numbers)

# Extend the 'numbers' list by adding elements from the 'fahad' list.
fahad = [12, 568, 876]
numbers.extend(fahad)
print(numbers)

# Concatenate 'numbers' and 'fahad' lists into a new list 'k'.
k = numbers + fahad
print(k)
