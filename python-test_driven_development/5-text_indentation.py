#!/usr/bin/python3
"""
This module contains a function that prints a text with 2 new lines after
each of these characters: '.', '?', and ':'.
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each of
    these characters: '.', '?', and ':'.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If 'text' is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    i = 0

    while i < len(text):
        result += text[i]
        if text[i] in ".?:":
            result += "\n\n"
            i += 1
            # Skip any spaces that may follow these characters
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1

    # Print the result without any leading/trailing spaces
    print(result.strip(), end="")
