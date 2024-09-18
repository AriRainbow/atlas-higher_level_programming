#!/usr/bin/python3
"""This module defines the Square class, which inherits from the Rectangle class.
It represents a square with a specific size attribute and provides methods
to calculate the area and a string representation of the square.

Classes:
    Square: A class representing a square with a size attribute validated by
            the integer_validator method from Rectangle.

Attributes:
    None

Methods:
    __init__(self, size): Initializes a new Square instance with the given size,
                            validated for positive integers.
    area(self): Returns the area of the square.
    __str__(self): Returns a string representation of the square.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size): Initializes a new Square instance.
        area(self): Calculates and returns the area of the square.
        __str__(self): Returns a string representation of the square.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Returns a string representation of the square.
 
        Returns:
            str: The string representation of the square.
        """
        return f"[Square] {self.__size}/{self.__size}"
