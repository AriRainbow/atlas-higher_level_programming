#!/usr/bin/python3
def uppercase(str):
    # loop through string
    for char in str:
        # check if lowercase
        if 97 <= ord(char) <= 122:
            # convert lowercase to uppercase
            char = chr(ord(char) - 32)
        # avoid new lines
        print("{}".format(char), end="")
    # print new line after loop
    print()
