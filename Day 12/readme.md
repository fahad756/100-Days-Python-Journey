# 100 Days of Coding - Day 12

## Recursion

Welcome to Day 12 of the 100 Days of Coding challenge! In this challenge, we will explore the concept of recursion in Python.

### Factorial using Recursion

The first part of the code demonstrates how to calculate the factorial of a number using recursion. The `factorial(n)` function is defined to calculate the factorial. If the number `n` is 0 or 1, the factorial is 1. Otherwise, the function recursively multiplies `n` with `factorial(n-1)` to compute the factorial.

### Example: Calculating the Factorial of 5

The code provides an example by calling the `factorial(5)` function to calculate the factorial of 5.

### Fibonacci Series using Recursion

The second part of the code demonstrates how to generate the Fibonacci series using recursion. The `fibonacci(i)` function is defined to generate the Fibonacci series. If the input `i` is 0, the function returns 0. If the input is 1, the function returns 1. For other values of `i`, the function calculates the Fibonacci series by summing the two previous numbers in the series using recursion (`fibonacci(i-1)` and `fibonacci(i-2)`).

### Example: Generating the Fibonacci Series for the First 10 Numbers

The code provides an example by using a loop to generate the first 10 numbers in the Fibonacci series and printing them.

### Explanation

Recursion is a powerful technique in programming, especially when dealing with problems that can be broken down into smaller subproblems. In the case of the factorial function, recursion simplifies the computation by reducing the problem to smaller subfactorials. Similarly, recursion makes it easier to generate the Fibonacci series by relying on previously computed values.

Remember that while recursion can be elegant and intuitive, it can also lead to performance issues if not used wisely. In some cases, iterative solutions might be more efficient.

## Resources

To learn more about recursion in Python and its applications, you can refer to the following resources:

- [Python Recursion - Programiz](https://www.programiz.com/python-programming/recursion)
- [Recursion - Real Python](https://realpython.com/python-recursion/)
- [Recursion in Python - GeeksforGeeks](https://www.geeksforgeeks.org/recursion-python/)

Happy learning and coding on Day 12 of the challenge! Keep up the great work!
