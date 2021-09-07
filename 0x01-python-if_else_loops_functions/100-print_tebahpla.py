#!/usr/bin/python3
i = 0
for c in range(65, 91):
    if c % 2 != 0:
        print("{:s}".format(chr(c + 57 - i)), end='')
        i = i + 1
    elif c % 2 == 0:
        print("{:s}".format(chr(c + 24 - i)), end='')
        i = i + 3
