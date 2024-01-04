#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

# Get the last digit of the number and preserve its sign
last_digit = abs(number) % 10 * (1 if number >= 0 else -1)

# Display the result
print(f"Last digit of {number} is {last_digit} and", end=" ")

# Check conditions and print additional information
if last_digit < 0:
    print("is less than 6 and not 0")
elif last_digit > 5:
    print("is greater than 5")
elif last_digit == 0:
    print("is 0")
else:
    print("is less than 6 and not 0")
