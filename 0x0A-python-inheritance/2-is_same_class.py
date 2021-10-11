#!/usr/bin/python3
"""
This module creates a function for checking objects
"""


def is_same_class(obj, a_class):
    """Check if an object is instance of a class"""
    if type(obj) is a_class:
        return True
    else:
        return False
