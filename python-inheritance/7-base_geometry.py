#!/usr/bin/python3
"""
This module defines a class BaseGeometry with
public methods 'area' and 'integer_validator'.
"""


class BaseGeometry:
    """
    BaseGeometry class: Contains methods for geometry operations.
    """

    def area(self):
        """
        Raises an exception indicating that the method is not implemented.
 
        Raises:
            Exception: Always raises an Exception with the message
            'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that 'value' is an integer greater than 0.

        Args:
            name (str): The name of the value (always a string).
            value (int): The value to be validated.

        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
