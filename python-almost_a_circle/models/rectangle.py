#!/usr/bin/python3
"""
Rectangle class that inherits from Base.
"""

Base = __import__('models.base').Base


class Rectangle(Base):
    """Represents a rectangle that inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.
        
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle's position.
            y (int): The y-coordinte of the rectangle's position.
            id (int): The id of the rectangle instance.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        self.__height = value

    @property
    def x(self):
        """Get the x-coordinate of the rectangle."""
        return self.__x
    
    @x.setter
    def x(self, value):
        """Set the x-coordinate of the rectangle."""
        self.__x = value

    @property
    def y(self):
        """Get the y-coordinate of the rectangle."""
        return self.__y
    
    @y.setter
    def y(self, value):
        """Set the y-coordinate of the rectangle."""
        self.__y = value
