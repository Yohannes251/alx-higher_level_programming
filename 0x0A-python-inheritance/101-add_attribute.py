#!/usr/bin/python3
"""
This module creates a function that adds a new attribute
"""


def add_attribute(self, name, value):
    """Adds a new attribute to object if possible"""
    if not hasattr(self, "__dict__") and not hasattr(self, "__slots__"):
        raise TypeError("can't add new attribute")
    if not hasattr(self, name) and hasattr(self, "__slots__"):
        raise TypeError("can't add new attribute")
    setattr(self, name, value)
