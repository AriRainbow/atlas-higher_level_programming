#!/usr/bin/python3
"""
This module defines a function to check if any object is
exactly an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Returns True if obj is exactly an instance of a_class.
    Otherwise, returns False.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of object against.

    Returns:
        bool: True if obj is exactly  an instance of a_class, False otherwise.
    """
    return type(obj) is a_class
