#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    # variables track best score and associated key
    best_key = None
    best_value = float('-inf')

    # find maximum value
    for key, value in a_dictionary.items():
        if value > best_value:
            best_value = value
            best_key = key

    return best_key
