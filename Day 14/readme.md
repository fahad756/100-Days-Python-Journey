# 100 Days of Coding - Day 14

## Python Dictionaries and Dictionary Methods

Welcome to Day 14 of the 100 Days of Coding challenge! In this session, we will explore Python dictionaries and learn about various dictionary methods.

### Dictionaries Overview

Dictionaries in Python are an unordered collection of key-value pairs. Each key in a dictionary maps to a corresponding value, allowing us to easily access values using their keys. Dictionaries are enclosed in curly braces `{}` and consist of comma-separated key-value pairs.

### Examples

1. Creating a Dictionary:
   - We demonstrate how to create a dictionary called 'details' with keys 'name', 'age', and 'Gender', and their respective values.
   - Output: `{'name': 'Fahad', 'age': 24, 'Gender': 'Male'}`

2. Printing Dictionary Keys and Values:
   - We show how to print all the keys and values of the 'details' dictionary.
   - Output: `dict_keys(['name', 'age', 'Gender'])`, `dict_values(['Fahad', 24, 'Male'])`

3. Accessing Dictionary Values:
   - We access the value corresponding to the key 'name' in the 'details' dictionary.
   - Output: `'Fahad'`

4. Iterating through a Dictionary:
   - We use a for loop to iterate through each key-value pair in the 'details' dictionary and print their values using formatted strings.
   - Output: `The value of name is Fahad`, `The value of age is 24`, `The value of Gender is Male`

### Dictionary Methods

1. Updating a Dictionary with Another Dictionary:
   - We create two dictionaries 'allusers' and 'user2', and then update 'allusers' with the key-value pairs from 'user2'.
   - Output: `{'un': 'fahad756', 'pass': '1122', 'username': 'Ali12', 'password': 'dsa3'}`

2. Removing a Key from a Dictionary:
   - We remove the key 'un' and its value from the 'allusers' dictionary using the `pop()` method.
   - Output: `{'pass': '1122', 'username': 'Ali12', 'password': 'dsa3'}`

3. Clearing and Emptying a Dictionary:
   - We demonstrate how to clear all key-value pairs from the 'allusers' dictionary, making it an empty dictionary, using the `clear()` method.
   - Output: `{}`

4. Deleting a Key-Value Pair from a Dictionary:
   - We delete the key 'pass' and its value from the 'allusers' dictionary using the `del` keyword.
   - Output: `{'un': 'fahad756'}`

### Explanation

Dictionaries are a powerful data structure in Python that allows us to store and access data using key-value pairs. They are useful for managing related pieces of information and can be dynamically modified using various built-in methods.

## Resources

To deepen your understanding of Python dictionaries and explore more dictionary methods, you can refer to the following resources:

- [Python Dictionaries - w3schools](https://www.w3schools.com/python/python_dictionaries.asp)
- [Python Dictionary Documentation - Python.org](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

Happy learning and coding on Day 14 of the challenge! Keep up the great work!
