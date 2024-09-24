#!/usr/bin/python3
"""
This module defines the Base class, which will be the "base" for all other classes.
"""

import json


class Base:
    """Represents the base model for all classes in this project."""

    __nb_objects = 0  # Private class attribute to track the number of objects.

    def __init__(self, id=None):
        """Initialize the Base class.

        Args:
            id (int): The id of the new instance.
                      If None, the id is auto-incremented.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dictionaries.
    
        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: The JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
