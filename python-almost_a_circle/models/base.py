#!/usr/bin/python3
"""
Base class for managing `id` attribute for inherited classes.
"""


class Base:
    """Represents the base model for managing the `id` attribute."""

    __nb_objects = 0  # Private class attribute to track the number of objects.
    
    def __init__(self, id=None):
        """Initialize the Base class.

        Args: id (int): The id of the new instance. If None, the id is auto-incremented.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
