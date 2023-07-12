import os

# If-Else Statements

# Prompt the user to enter their age
age = int(input("Enter Your Age Please: "))

# Different Operators
# age <=
# age ==
# age >=
# age !=
# age <
# age >

# Check if the age is less than 18
if age < 18:
    print("Your Age Is Less Than 18. You are not eligible")
else:
    print("You're Eligible ")

# Nested If-Else Statements

# Prompt the user to enter a number
number = int(input("Enter Any Number: "))

# Check if the number is less than 0
if number < 0:
    print("Number is less than 0")

# Check if the number is greater than 0
elif number > 0:
    print("Number is greater than 0")

    # Check if the number is equal to 5
    if number == 5:
        print("Number is equal to five")

    # Check if the number is between 5 and 100
    elif number > 5 and number < 100:
        print("Number is between 5-100")

# If the number is not less than 0 and not greater than 0, it must be zero
else:
    print("Number is zero")

# Match Case Statements

# Check the Python version using the operating system command
os.system("python --version")

# Prompt the user to enter a number
x = input("Please Enter Number: ")

# Perform actions based on the entered number using match case statements (Python 3.10+)
match x:
    case 4:
        print("The number is 4")
    case 1:
        print("The number is 1")
