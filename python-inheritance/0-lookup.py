#!/usr/bin/python3
"""
This module defines a finction lookup which
returns the list of available attributes and methodsof an object.
"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object."""
    return dir(obj)
