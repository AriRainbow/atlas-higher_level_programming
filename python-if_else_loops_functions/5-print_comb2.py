#!/usr/bin/python3
# Loop through numbers from 0 to 99
for number in range(100):
    # Check if it is last number
    if number == 99:
        print("{:02d}".format(number))
    else:
        print("{:02d}, ".format(number), end="")
