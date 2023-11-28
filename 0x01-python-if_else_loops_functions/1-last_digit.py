#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastdigit = (number * -1) % 10
    message = "and is less than 6 and not zero"
    print(f"Last digit of {number} is -{lastdigit} {message}")
else:
    lastdigit = number % 10
    if (lastdigit > 5):
        message = "and is greater than 5"
    elif (lastdigit == 0):
        message = "and is 0"
    else:
        message = "and is less than 6 and not zero"
    print(f"Last digit of {number} is {lastdigit} {message}")
