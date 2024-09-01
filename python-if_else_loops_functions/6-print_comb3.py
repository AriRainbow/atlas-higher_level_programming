#!/usr/bin/python3
# loop through first digit
for d_1 in range(0, 10):
    # loop through second digit d_2 > d_1
    for d_2 in range(d_1 + 1, 10):
        # print combination of both digits, formatted as 2 digits
        if d_1 == 8 and d_2 == 9:  # checking if last combination
            print("{}{}".format(d_1, d_2))  # no comma or space
        else:
            print("{}{}, ".format(d_1, d_2), end="")
