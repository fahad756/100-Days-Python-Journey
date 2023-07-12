import time
import os

# Get current time in the format HH:MM:SS
TimeFormat = time.strftime("%H:%M:%S")
print(TimeFormat)

# Extract the hour from the current time
Hour = int(time.strftime("%H"))
print(Hour)

# Check the hour value and print a corresponding greeting
if Hour < 12 and Hour >= 6:
    print("Good Morning!")
elif Hour >= 12 and Hour < 18:
    print("Good Afternoon!")
elif Hour >= 18 or Hour < 6:
    print("Good Night!")

