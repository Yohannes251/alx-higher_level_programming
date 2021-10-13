#!/usr/bin/python3
"""
This module creates a function that reads a file
"""


def read_file(filename=""):
    """Reads and prints a file"""
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
