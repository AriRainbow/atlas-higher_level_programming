#!/usr/bin/python3
"""
This module defines the Square class, which inherits from Rectangle.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialze a new Square.

        Args:
            size (int): The size of the square.
            x (int): The x-coordinate of the square's position.
            y (int): The y-coordinate of the square's position.
            id (int): The id of the square instance.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square, validating that it's an integer > 0."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the square attributes using *args and **kwarg.

        Args:
            *args: No-Keyworded arguments to update attribites (id, size, x, y).
            **kwargs: Keyworded arguments to update attributes.
        """
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                if key in ['id', 'size', 'x', 'y']:
                    setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def to_dictionary(self):
        """Return the dictionary representation of the Square.
  
        Returns:
            dict: A dictionary containing id, size, x, and y.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
