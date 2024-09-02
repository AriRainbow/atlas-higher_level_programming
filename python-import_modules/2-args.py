#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # get number of args
    num_args = len(sys.argv) - 1

    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_args))

    # print each arg with position
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
