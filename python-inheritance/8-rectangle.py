#!/usr/bin/python3

BaseGeometry = __import__('7-_base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle class inheriting from BaseGeometry"""

    def __init__(self, width, height):
        """Initializing a new Rectangle
 
        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
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
