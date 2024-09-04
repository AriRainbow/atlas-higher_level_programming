#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # retrieve keys and sort alphabetically
    for key in sorted(a_dictionary.keys()):
        # in sorted order
        print("{}: {}".format(key, a_dictionary[key]))