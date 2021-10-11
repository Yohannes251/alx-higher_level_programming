#!/usr/bin/python3
"""
This module adds additional functionality to list class
"""


class MyList(list):
    """Class defines a function for printing sorted list"""
    def print_sorted(self):
        print(sorted(self))
