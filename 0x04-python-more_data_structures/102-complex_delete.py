#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dicti = dict(a_dictionary)
    if value in list(a_dictionary.values()):
        for key, val in dicti.items():
            if val == value:
                a_dictionary.pop(key)
        return a_dictionary
    return a_dictionary
