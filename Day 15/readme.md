# Day 15: Using `while` Loop with `else`

This code example demonstrates the use of a `while` loop with an `else` statement in Python. In Python, the `else` statement can be used with both `for` and `while` loops to specify a block of code that should execute when the loop completes normally (without encountering a `break` statement).

## Code Explanation

1. Initialize variables: `i` is set to 4, and `x` is set to 0.
2. There's a commented-out example of using `else` with a `for` loop, but it's not used in the current program.
3. The main part of the example is the `while` loop:
   - The loop runs as long as the value of `x` is less than 7.
   - Inside the loop, the current value of `x` is printed, and `x` is incremented by 1.
   - An `if` statement checks if `x` is equal to 3. If it is, the loop is terminated using the `break` statement.
   - Since `x` is incremented by 1 after being printed, the loop will terminate when `x` becomes 3.
4. After the `while` loop, there's an `else` block associated with it. However, in this example, the `else` block won't execute because the loop was exited prematurely by the `break` statement.

## Usage

To run the code, make sure you have Python installed. Copy and paste the provided code into a Python script or interpreter, and then execute it. You should see the output of the loop iterations, but the "Loop ended" message in the `else` block won't be displayed due to the early termination.

Feel free to modify the code and experiment with different values of `x` and `i` to observe how the loop behaves.

## Further Reading

- [Python Loops and Control Statements](https://docs.python.org/3/tutorial/controlflow.html)
- [Understanding the `else` Clause in Loops](https://www.geeksforgeeks.org/using-else-conditional-statement-with-for-loop-in-python/)
