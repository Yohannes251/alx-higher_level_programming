#!/usr/bin/python3
def print_last_digit(number):
    numstr = str(number)
    num = int(numstr[len(numstr) - 1])
    print("{:d}".format(num), end='')
    return num
