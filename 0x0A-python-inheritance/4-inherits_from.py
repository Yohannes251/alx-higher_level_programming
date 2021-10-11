#!/usr/bin/python3
"""
This module creates a function that compares an object with a class
"""


def inherits_from(obj, a_class):
    """Checks if an object is instance of a class inherited from given class"""
    if a_class != type(obj):
        if isinstance(obj, type(obj)) and issubclass(type(obj), a_class):
            return True
    else:
        return False
