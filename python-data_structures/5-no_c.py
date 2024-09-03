#!/usr/bin/python3
def no_c(my_string):
    # initialize empty string to store result
    new_string = ""

    for char in my_string:
        # add character, not c
        if char != 'c' and char != 'C':
            new_string += char

    # return resulting string
    return new_string
