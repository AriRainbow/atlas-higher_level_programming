#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # copy original list
    new_list = my_list[:]

    # is index valid
    if 0 <= idx < len(my_list):
        new_list[idx] = element

    # new list, either modified or copy of original
    return new_list
