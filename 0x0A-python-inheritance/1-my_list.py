#!/usr/bin/python3
"""
This module adds additional functionality to list class
"""


class MyList(list):
    def print_sorted(self):
        print("{}".format(sorted(self)))
