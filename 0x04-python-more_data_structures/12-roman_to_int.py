#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) is False or roman_string is None:
        return 0
    roman_int = 0
    for char in roman_string:
        if char == 'I':
            roman_int += 1
        elif char == 'V':
            roman_int += 5
        elif char == 'X':
            roman_int += 10
        elif char == 'L':
            roman_int += 50
        elif char == 'C':
            roman_int += 100
        elif char == 'D':
            roman_int += 500
        elif char == 'M':
            roman_int += 1000
    return roman_int
