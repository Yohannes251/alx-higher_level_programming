#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    string = ''
    for c in str:
        if i != n:
            string += str[i]
        i += 1
    return string
