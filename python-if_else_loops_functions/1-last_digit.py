#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"Last digit of {number} is {abs(number % 10)} and is ", end = "")
if number == 0:
    print(0)
elif number % 10 > 5:
    print("greater than 5")
else:
    print("less than 6 and not 0")
