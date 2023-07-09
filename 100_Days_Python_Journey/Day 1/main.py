#Basic Concepts Day 1

# Print "Hello World"
print("Hello World")

# Use the escape character "\n" to break the line and print in a new line
print('You can break a line using the "\\n" escape character.')

# Use the "sep" parameter to add a "~" between each value
print("Hey", 6, 7, sep='~', end='009\n')


##### VARIABLES ##############

# Integer variable
a = 1
print(a)

# String variable
name = "Fahad"
print(name)

# Boolean variable
is_true = True
print(is_true)

# Sum of two integers
b = 5
sum = a + b
print(sum)

# Concatenation of strings
last_name = "Waseem"
full_name = name + " " + last_name
print(full_name)

# Print the types of variables
print("Type of name:", type(name))
print("Type of is_true:", type(is_true))
print("Type of a:", type(a))

##### PYTHON DATA TYPES ##############

# List -> You can define any data type in a list, and you can add or remove elements dynamically
my_list = [1, "Two", [3, 4], 5.5]
print(my_list)
print(type(my_list))

# Tuple -> Similar to a list, but it is immutable (cannot be modified once created)
my_tuple = (1, 2, "Three", (4, 5))
print(my_tuple)
print(type(my_tuple))


#Opertaors
add = 15 + 6
print(add)
subtract = 15-6
print(subtract)
devision = 15/6
print(devision)
multiply = 15*6
print(devision)
modulus = 15%6
print(modulus)
