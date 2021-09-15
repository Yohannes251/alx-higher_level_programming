#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) is False or roman_string is None:
        return 0
    s = roman_string[:]
    roman_int = 0
    i = 0
    for i in range(0, len(s)):
        if s[i] == 'I':
            if i < len(s) - 1:
                if s[i + 1] in ['V', 'X']:
                    roman_int -= 1
                else:
                    roman_int += 1
            else:
                roman_int += 1
        elif s[i] == 'V':
            roman_int += 5
        elif s[i] == 'X':
            if i < len(s) - 1:
                if s[i + 1] in 'LMC':
                    roman_int -= 10
                else:
                    roman_int += 10
            else:
                roman_int += 10
        elif s[i] == 'L':
            roman_int += 50
        elif s[i] == 'C':
            roman_int += 100
        elif s[i] == 'D':
            roman_int += 500
        elif s[i] == 'M':
            roman_int += 1000
        i += 1
    return roman_int
