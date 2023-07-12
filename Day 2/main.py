# Type Casting

# Concept: Type casting is the process of converting one data type into another.
# It allows you to change the interpretation or representation of data.

# Example 1: Concatenating strings
a = "1"
b = "2"
print(a + b)  # Output: "12"
# Explanation: Since both variables 'a' and 'b' are defined as strings,
# using the '+' operator concatenates the two strings, resulting in "12".

# Example 2: Adding integers
a = 1
b = 2
print(a + b)  # Output: 3
# Explanation: Here, 'a' and 'b' are defined as integers.
# Using the '+' operator performs addition, resulting in the sum of 1 and 2, which is 3.

# Conversion example: Converting strings to integers
a = "1"
b = "2"
print(int(a) + int(b))  # Output: 3
# Explanation: The 'int()' function is used to convert the string values of 'a' and 'b' into integers.
# After conversion, the '+' operator performs addition, resulting in the sum of 1 and 2, which is 3.

# Types of type casting

# Explicit type casting
string = "12"
integer = 2
print("The sum of String and Integer after typecasting:", int(string) + integer)
# Explanation: Explicit type casting is done manually using functions like 'int()', 'float()', 'str()', etc.
# In this example, the 'int()' function is used to convert the string 'string' into an integer.
# The sum of the converted integer and the 'integer' variable is printed.

# Implicit type casting
a = 1.5
print(type(a))  # Output: <class 'float'>
b = 1
print(type(b))  # Output: <class 'int'>
c = a + b
print(c)  # Output: 2.5
print(type(c))  # Output: <class 'float'>
# Explanation: Implicit type casting, also known as automatic type conversion, is performed by Python itself.
# In this example, 'a' is a floating-point number and 'b' is an integer.
# When the '+' operator is used to add them, Python automatically converts 'b' to a float and performs the addition.
# The result is 2.5, which is a float.
# The type of 'c' is printed to confirm the data type.


#Input Values
FirstName = input("What is your First name? ")
LastName = input("What is your Last Name? ")
print(FirstName +" "+ LastName)


