#!/usr/bin/python3
"""
This module defines the Base class,
which will be the "base" for all other classes.
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

    @classmethod
    def save_to_file(cls, list_objs):
        """Save the JSON string representation of list_onjs to a file.

        Args:
            list_objs (list): A list of instances that inherit from Base (Rectangle or Square).
        """
        filename = f"{cls.__name__}.json"
        list_dicts = []  # Initializes an empty list to store dictionary representations

        # Converts each object in list_objs to its dictionary representation
        if list_objs is not None:
            for obj in list_objs:
                if hasattr(obj, "to_dictionary"):
                    list_dicts.append(obj.to_dictionary())
                else:
                    raise AttributeError(f"{obj} does not have a to_dictionary method")

        # Convert the list of dictionaries to a JSON string
        json_string = cls.to_json_string(list_dicts)

        # Write the JSON string to the file
        with open(filename, "w") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by the JSON string.

        Args:
            json_string (str): A string representing a list of dictionaries.

        Returns:
            list: The list represented by json_string, or an empty list if json_string is None or empty.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with all attributes already set using the dictionary.
 
        Args:
            **dictionary (dict): A dictionary of attributes for the instance.

        Returns:
            obj: A new instance with updated attributes.
        """
        if cls.__name__ == "Rectangle":
            # Create a dummy Rectangle instance with default values
            dummy = cls(1, 1)  # Dummy width, height
        elif cls.__name__ == "Square":
            # Create a dummy Square instance with default values
            dummy = cls(1)  # Dummy size

        # Update the dummy instance with real values from the dictionary
        dummy.update(**dictionary)

        return dummy
