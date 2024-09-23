#!/usr/bin/python3
"""
Base class for managing id attribute.
"""


class Base:
    """Represents the base model."""

    __nb_objects = 0 # Private class attribute to keep track of the number of objects
    
    def __init__(self, id=None):
        """Initialize the Base class with id or auto-increment."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
