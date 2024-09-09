#!/usr/bin/python3
"""
This module contains a function that prints a square using the character '#'.
"""


def print_square(size):
    """
    Prints a square of size 'size' using the character '#'.

    Args:
        size (int): The size of the square (length of each side).

    Raises:
        TypeError: If 'size' is not an integer.
        ValueError: If 'size' is less than 0.
        TypeError: If 'size' is a float and less than 0.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    
    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    
    for _ in range(size):
        print("#" * size)