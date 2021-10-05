#!/usr/bin/python3
"""
This module defines a locked class
"""


class LockedClass:
    """Prevents dynamical creation of new instance attributes"""

    __slots__ = ['first_name']
