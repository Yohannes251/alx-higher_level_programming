#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    maximum = max(list(a_dictionary.values()))
    for key, value in a_dictionary.items():
        if value == maximum:
            return key
