#!/usr/bin/python3
"""
This module creates a function that compares an object with a class
"""


def inherits_from(obj, a_class):
    """Checks if an object is instance of a class inherited from given class"""
    if a_class != type(obj):
        return issubclass(type(obj), a_class)
    else:
        return False
