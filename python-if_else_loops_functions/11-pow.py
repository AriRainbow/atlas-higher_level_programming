#!/usr/bin/python3
def pow(a, b):
    # return reciprocal of raised to positive exponent
    if b < 0:
        return 1 / (a ** abs(b))
    else:
        return a ** b
