# Initialize the value of 'i' to 4 and 'x' to 0
i = 4
x = 0

# The following code is commented out; it's an example of using 'else' with a 'for' loop
# In this example, 'x' would iterate over the range 0 to (i-1), and after the loop finishes, the 'else' block would execute
# However, this code is not used in the current program

# for x in range(i):
#     print(x)
# else:
#     print("Loop ended")

# The while loop starts here; it will continue executing as long as 'x' is less than 7
while x < 7:
    # Print the current value of 'x'
    print(x)
    # Increment the value of 'x' by 1
    x += 1

    # Check if the value of 'x' is equal to 3
    if x == 3:
        # If 'x' is 3, break out of the loop (stop the loop's execution)
        break
else:
    # The 'else' block for the while loop
    # This block will not execute in this case because the loop was exited using 'break'
    print("Loop ended")
