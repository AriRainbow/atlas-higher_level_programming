#!/usr/bin/python3
"""
This module contains the finction add_integer.
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats (after casting to integers).

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number, default is 98.

    Returns:
        int: The sum of a and b after casting to integers.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    # cast floats to integers
    a = int(a)
    b = int(b)

    return a + b