#!/usr/bin/python3
"""
This module implements listing of contents of an object
"""


def lookup(obj):
    """Returns list of attributes and methods of an object"""
    return dir(obj)
