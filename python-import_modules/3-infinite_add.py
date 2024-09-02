#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # initialize variable to hold sum
    total = 0

    # loop starting from index 1
    for i in range(1, len(sys.argv)):
        total += int(sys.argv[i])

    # print total sum
    print(total)
