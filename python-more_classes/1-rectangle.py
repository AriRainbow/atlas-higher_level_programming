#!/usr/bin/python3
"""
This module defines a Rectangle class with width and heigth attributes,
along with propert setters and getters for validation.
"""


class Rectangle:
    """A class used to represent a rectangle.

    Attributes:
    ----------
    width : int
        The width of the rectangle (default is 0).
    height : int
        The height of the rectangle (default is 0).
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the Rectangle with optional width and height.

        Args:
        width (int): The width of the rectangle (default is 0).
        height (int): The height of the rectangle (default is 0).
        """
        self.width = width  # This will call the setter
        self.height = height  # This will call the setter

    @property
    def width(self):
        """Getter for width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute. Ensures it's an integer and >= 0."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute.
        Ensures it's an integer and >= 0."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
