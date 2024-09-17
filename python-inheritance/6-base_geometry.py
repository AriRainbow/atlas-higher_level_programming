#!/usr/bin/python3
"""
This module defines a class of BaseGeometry with a public method 'area'
that raises an exception.
"""


class BaseGeometry:
    """
    BaseGeometry class: Contains a method that raises an exception.
    """

    def area(self):
        """
        Raises an exception indicating that the method is not implemented.

        Raises:
            Exception: Always raises an Exception with the message
            'area() is not implemented'.
        """
        raise Exception("area() is not implemented")
