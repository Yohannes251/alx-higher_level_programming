#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last = number % 10
else:
    last = (abs(number) % 10) * -1
string = "Last digit of {0} is {1} and is "
if number < 0 and last != 0:
    print(string.format(number, last) + "less than 6 and not 0")
elif last > 5:
    print(string.format(number, last) + "greater than 5")
elif last == 0:
    print(string.format(number, last) + "0")
else:
    print(string.format(number, last) + "less than 6 and not 0")
