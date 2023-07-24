# Recursion

# Function to calculate factorial using recursion
def factorial(n):
    ''' This function calculates the factorial of a number using recursion.
        If the number is 0 or 1, the factorial is 1.
        Otherwise, it calculates the factorial using n * factorial(n-1).'''
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Example: Calculating the factorial of 5
print(factorial(5))


# Function to generate Fibonacci series using recursion
def fibonacci(i):
    ''' This function generates the Fibonacci series using recursion.
        If the input is 0, the function returns 0.
        If the input is 1, the function returns 1.
        For other values, the function calculates the Fibonacci series using the sum of the previous two numbers.'''
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fibonacci(i-1) + fibonacci(i-2)

# Example: Generating the Fibonacci series for the first 10 numbers
for i in range(10):
    print(fibonacci(i))
