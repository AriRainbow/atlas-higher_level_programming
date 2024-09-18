#!/usr/bin/python3
"""
This module defines a function that writes an Object to a text file,
using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file using its JSON representation.

    Args:
        my_obj (object): The object to serialize and write to the file.
        filename (str): The name of the file to write the JSON data into.
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
