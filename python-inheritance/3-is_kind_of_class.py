#!/usr/bin/python3
"""
This module provides a function that checks if an object is an instance of
a given class or an instance of a class that inherited from the given class.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an onstance of a_class or a class
    that inherited from a_class.
    Otherwise, returns False.

    Args:
        obj: The object to check.
        a_class: The class to compair with.

    Returns:
        bool: True if obj is an instance of, or inherited from a_class.
        False otherwise.
    """
    return isinstance(obj, a_class)
