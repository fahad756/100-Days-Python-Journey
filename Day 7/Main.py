# Break & Continue
for i in range(20):
    if i == 10:
        break  # Exit the loop when i equals 10
    print("5 *", i + 1, "= ", 5 * (i + 1))

for i in range(12):
    if i == 10:
        print("Skipping iteration")
        continue  # Skip the rest of the code in the current iteration and move to the next iteration
    print("5 *", i, "= ", 5 * i)

print("FUNCTIONS")

# Functions
def Addition(a, b):
    print(a, "+", b, "=", a + b)

def temp(d):
    pass  # Placeholder function that does nothing

Addition(5, 5)
temp(5)

# Passing Arguments

def avg(*numbers):
    # *numbers = tuple
    sum = 0
    for i in numbers:
        sum += i
    print("Length:", len(numbers))
    print("The average is", sum / len(numbers))

avg(2, 6)

def names(**names):
    print("Hello", names["fname"], names["lname"])

names(fname="Fahad", lname="Waseem")

def justreturn(a, b):
    c = a + b
    return c

value = justreturn("3", "5")
print(value)
