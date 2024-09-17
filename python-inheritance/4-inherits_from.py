#!/usr/bin/python3
"""
This module provides a finction to check if an object is an instance of a class
that inherited (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Returns true if obj is an instance of a class
    that inherited (directly or indirectly)
    from a_class. Otherwise, returns False.

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        bool: True if obj is an instance of a subclass of a_class,
        excluding direct instancesof a_class.
    """
    return isinstance(obj, a_class) and not type(obj) is a_class
