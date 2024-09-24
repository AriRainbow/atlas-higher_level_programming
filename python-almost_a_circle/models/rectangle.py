#!/usr/bin/python3
"""
This module defines the Rectangle class, which inherits from Base.

This module provides a Rectangle class with attributes for width, height,
x and y coordinates, along with their respective getters and setters.
"""

from models.base import Base


class Rectangle(Base):
    """Represents a rectangle that inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle's position.
            y (int): The y-coordinate of the rectangle's position.
            id (int): The id of the rectangle instance.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation."""
        self.validate_integer(value, "width")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""

        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectanglen with validation."""
        self.validate_integer(value, "height")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x-coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x-coordinate of the rectangle with validation."""
        self.validate_integer(value, "x")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the y-coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y-coordinate of the rectangle with validation."""
        self.validate_integer(value, "y")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def validate_integer(self, value, name):
        """Validate that value is an integer."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

    def area(self):
        """Calculates the area of the rectangle.

        Returns:
            The area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """Prints the rectangle using the '#' character, considering x and y coordinates."""
        print("\n" * self.y, end='')  # Print y new lines
        for _ in range(self.height):
            print(' ' * self.x + '#' * self.width)  # Print x spaces followed by #

    def __str__(self):
        """Return a string representation of the Rectangle."""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Update the rectangle attributes based on the given arguments.

        Args:
            *args: Non-keyworded arguments to update attributes.
            **kwargs: Keyworded arguments to update attributes.
        """
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)

        for key, value in kwargs.items():
            if key in ['id', 'width', 'height', 'x', 'y']:
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of the Rectangle.

        Returns:
            dict: A dictionary containing id, width, height, x, and y.
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
