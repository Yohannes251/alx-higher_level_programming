#!/usr/bin/python3
"""
This module creates a function that writes to a file
"""


def write_file(filename="", text=""):
    """"Writes to a file a returns written characters"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
