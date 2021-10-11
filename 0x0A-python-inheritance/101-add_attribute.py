#!/usr/bin/python3
"""
This module creates a function that adds a new attribute
"""


def add_attribute(self, name, value):
    if isinstance(self, type):
        self.name = value
    else:
        raise TypeError("can't add new attribute")
