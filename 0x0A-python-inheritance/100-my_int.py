#!/usr/bin/python3
"""
This module extends the int class
"""


class MyInt(int):
    """Inverts == and != operators"""

    def __eq__(self, other):
        """Inverts == operator"""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """Inverts != operator"""
        return int.__eq__(self, other)
