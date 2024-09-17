#!/usr/bin/python3
"""
This module defines the Rectangle class, which inherits from the BaseGeometry class.
It represents a rectangle with specific width and height attributes.

Classes:
    Rectangle: A class representing a rectangle, with width and height attributes
                validated by the integer_validator method from BaseGeometry.
                
Attributes:
    None
    
Methods:
    __init__(self, width, height): Initializes a new Rectangle instance with the given
                                    width and height, validated for positive integers.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Rectangle class inheriting from BaseGeometry.
    
    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
        
    Methods:
        __init(self, width, height): Initializes a new Rectangle instance.
    """

    def __init__(self, width, height):
        """
        Initializing a new Rectangle
 
        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def __str__(self):
        """Return the string representation of the Rectanngle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """Return the area of the Rectangle"""
        return self.__width * self.__height
