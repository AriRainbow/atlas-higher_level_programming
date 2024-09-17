#!/usr/bin/python3
"""
This module defines the Rectangle class, which inherits from the BaseGeometry class.
It represents a rectangle with specific width and height attributes and provides
methods to calculate the area and a string representation of the rectangle.

Classes:
    Rectangle: A class representing a rectangle with wodth and height attributes
                validated by the integer_validator method from BaseGeometry.

Attributes:
    None

Methods:
    __init__(self, width, height): Initializes a new Rectangle instance with the given
                                    width and height, validated for positive integers.
    area(self): Returns the area of the rectangle.
    __str__(self): Returns a string representation of the rectangle.
"""
BaseGeometry = __import__('7-base_geometry').BaseGemetry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    
    Methods:
        __init__(self, width, height): Initializes a new Rectangle instance.
        area(self): Calculates and returns the area of the rectangle.
        __str__(self): Returns a string representation of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
   
        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.height = height

    def area(self):
        """
        Calculates the area of the rectangle.
  
        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        
        Returns:
            str: The string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
