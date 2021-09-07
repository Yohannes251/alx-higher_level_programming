#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numstr = str(number)
num = int(numstr[len(numstr) - 1])
string = "Last digit of {0} is {1} and is "
if num > 5:
    print(string.format(number, num) + "greater than 5")
elif num == 0:
    print(string.format(number, num) + "0")
else:
    print(string.format(number, num) + "less than 6 and not 0")
