#!/usr/bin/python3
def uniq_add(my_list=[]):
    # convert to set to remove duplicates
    unique_numbers = set(my_list)
    return sum(unique_numbers)
