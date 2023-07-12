# Loops

# For loop
name = 'Fahad Waseem'
for i in name:  # Iterating over each character in the string 'name'
    print(i)  # Printing each character

colors = ['pink', 'grey', 'Red', 'Black']
for color in colors:  # Iterating over each element in the list 'colors'
    print(color)  # Printing each element

for i in range(3):  # Looping 3 times, starting from 0 (default starting value)
    print(i)  # Printing the current value of 'i'

for i in range(1, 8, 2):  # Looping from 1 to 7 (exclusive) with a step size of 2
    print(i)  # Printing the current value of 'i'

print("While Loops From here")

# While Loop
i = 0
while i < 3:  # Executing the loop until 'i' is less than 3
    print(i)  # Printing the current value of 'i'
    i += 1  # Incrementing 'i' by 1 in each iteration

print("Decrement Loop")
i = 5
while i > 0:  # Executing the loop until 'i' is greater than 0
    print(i)  # Printing the current value of 'i'
    i -= 1  # Decrementing 'i' by 1 in each iteration
else:
    print("While Loop Ended")  # Printing "While Loop Ended" after the loop completes

# do{
#
# }while(condition);

i = 0
while True:  # Creating an infinite loop
    print(i)  # Printing the current value of 'i'
    i += 1  # Incrementing 'i' by 1 in each iteration
    if i % 100 == 0:  # Checking if 'i' is divisible by 100
        break  # Breaking out of the loop if the condition is met
