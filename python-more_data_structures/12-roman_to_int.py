#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    # mapping roman numerals to integers
    roman_to_int_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    # process each character
    for char in roman_string:
        if char not in roman_to_int_map:
            return 0

        current_value = roman_to_int_map[char]

        # if prev value is less than current value
        if prev_value < current_value:
            total += current_value - 2 * prev_value
        else:
            total += current_value

        prev_value = current_value

    return total
