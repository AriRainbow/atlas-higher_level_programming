#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list
"""


class MyList(list):
    """
    A class that inherits from a list and adds a method
    to print the list in sorted order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order without modifying the original list.
        """
        print(sorted(self))
