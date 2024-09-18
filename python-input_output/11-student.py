#!/usr/bin/python3
"""
This module defines the Student class with methods for JSON serialization and deserialization.
"""


class Student:
    """
    A class to represent a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns the dictionary representation of the Student instance.
        If attrs is a list of strings, only attributes listed in attrs are included.

        Args:
            attrs (list, optional): A list of attribute names to include in the dictionary.
        
        Returns:
            dict: The dictionary representation of the student.
        """
        if attrs is None:
            return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
            }
       
        # Ensure attrs is a list of strings and contains valid attributes
        if not isinstance(attrs, list) or not all(isinstance(attr, str) for attr in attrs):
            return {}
       
        # Construct the dictionary based on attrs
        return {key: getattr(self, key) for key in attrs if hasattr(self, key)}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with values from the provided dictionary.

        Args:
            json (dict): A dictionary containing attribute names and values to update the student.
        """
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
