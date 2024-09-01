#!/usr/bin/python3
def uppercase(str):
    result = ""

    for char in str:
        if 97 <= ord(char) <= 122:
            char = chr(ord(char) - 32)
        result += "{}".format(char)

    print("{}".format(result))
