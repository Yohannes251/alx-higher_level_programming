#!/usr/bin/python3
def magic_string(c=[0]):
    c[0] += 1
    return ("Holberton, " * c[0])[:-2]
