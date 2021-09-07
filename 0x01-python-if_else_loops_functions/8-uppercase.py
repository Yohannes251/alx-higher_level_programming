#!/usr/bin/python3
def uppercase(str):
    i = len(str)
    for c in str:
        if 97 <= ord(c) <= 122:
            str += chr(ord(c) - 32)
        else:
            str += c
    print("{:s}".format(str[i:]))
