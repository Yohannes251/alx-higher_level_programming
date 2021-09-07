#!/usr/bin/python3
for c in range(0, 9):
    for x in range(c + 1, 10):
        if c != 8:
            print("{0:d}{1:d}".format(c, x), end=', ')
        else:
            print("{0:d}{1:d}".format(c, x))
