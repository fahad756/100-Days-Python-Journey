# Dictionaries

# Create a dictionary called 'details' with keys 'name', 'age', and 'Gender', and corresponding values 'Fahad', 24, and 'Male'.
details = {'name': 'Fahad', 'age': 24, 'Gender': 'Male'}

# Print the entire dictionary 'details'.
print(details)

# Print all the keys of the dictionary 'details'.
print(details.keys())

# Print all the values of the dictionary 'details'.
print(details.values())

# Print the value corresponding to the key 'name' in the dictionary 'details'.
print(details['name'])

# Iterate through each key (val) in the dictionary 'details' and print the key and its corresponding value using formatted string.
for val in details:
    print(f"The value of {val} is {details[val]}")

# Dictionary Methods

# Create an empty dictionary called 'allusers'.
# Commented out, not in use.

# Create a dictionary 'allusers' with keys 'un' and 'pass', and corresponding values 'fahad756' and '1122'.
allusers = {'un': 'fahad756', 'pass': '1122'}

# Create a dictionary 'user2' with keys 'username' and 'password', and corresponding values 'Ali12' and 'dsa3'.
user2 = {'username': 'Ali12', 'password': 'dsa3'}

# Update the 'allusers' dictionary by adding the key-value pairs from 'user2' dictionary to it.
allusers.update(user2)

# Print the updated 'allusers' dictionary.
print(allusers)

# Remove the key-value pair with the key 'un' from the 'allusers' dictionary.
allusers.pop('un')

# Print the 'allusers' dictionary after removing the 'un' key-value pair.
print(allusers)

# Clear all the key-value pairs from the 'allusers' dictionary, making it an empty dictionary.
allusers.clear()

# Print the 'allusers' dictionary after clearing it (which will show an empty dictionary).
print(allusers)

# Reassign the 'allusers' dictionary with the keys 'un' and 'pass' and their corresponding values.
allusers = {'un': 'fahad756', 'pass': '1122'}

# Delete the key 'pass' and its corresponding value from the 'allusers' dictionary.
del allusers['pass']

# Print the 'allusers' dictionary after deleting the 'pass' key-value pair.
print(allusers)
