#!/usr/bin/python3
# import
from calculator_1 import add, sub, mul, div

# assign values
a = 10
b = 5

# perform and print
print("{} + {} = {}".format(a, b, add(a, b)))
print("{} - {} = {}".format(a, b, sub(a, b)))
print("{} * {} = {}".format(a, b, mul(a, b)))
print("{} / {} = {}".format(a, b, div(a, b)))

# runs only when executed directly
if __name__ == "__main__":
    pass
