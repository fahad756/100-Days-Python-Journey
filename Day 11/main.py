# F-Strings

# F-Strings are a new way of formatting strings in Python introduced in Python 3.6.
# They are more concise and convenient compared to the older `.format()` method.

# Example 1: Using .format() method to format a string with variables
letter = "My Name is {} and I am from {}"
city = "Lahore"
name = "Fahad"
print(letter.format(name, city))

# Example 2: Using F-Strings to format a string with variables
print(f"My name is {name} and I am from {city}")

# F-Strings also support formatting numerical values.
# Example 3: Formatting a float with F-String and limiting decimal places to 2
apple = 23.77001
price = f"The price of this apple is {apple:.2f}"
print(price)

# F-Strings allow escaping curly braces by doubling them, useful for displaying literal braces.
# Example 4: Using doubled curly braces in F-String
use = f"This is how you use fstring My name is {{Name}} and I am {{age}} years old!"
print(use)


# Docstrings

# Docstrings are used to provide documentation for functions, modules, and classes in Python.
# They are enclosed within triple quotes and appear as the first statement in the function or module.

# Example: A function with a docstring to explain its purpose
def root(n):
    ''' This is a docstring, and this function is used to calculate the square of a number.'''
    print(n ** 2)

# Calling the function and displaying the docstring using __doc__ attribute
root(5)
print(root.__doc__)


# PEP 8 - Python Enhancement Proposal 8

# PEP 8 is a style guide for writing Python code, which recommends a consistent and readable coding style.
# Following PEP 8 guidelines improves code readability and maintainability.

# Zen of Python
# Python has a set of guiding principles referred to as the "Zen of Python."
# These principles are presented as a series of aphorisms that promote a simple and readable coding style.
# To view them, you can use the "import this" command in Python.
