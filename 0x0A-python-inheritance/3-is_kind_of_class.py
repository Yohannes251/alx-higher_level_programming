#!/usr/bin/python3
"""
This module creates a function that compares an object with a class
"""


def is_kind_of_class(obj, a_class):
    """Returns boolean value OF whether an object is instance of a class"""
    return isinstance(obj, a_class)
