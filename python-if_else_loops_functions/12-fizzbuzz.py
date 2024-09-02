#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 101):
        # check if multiple of 3 AND 5
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz", end=" ")
        # check if multiple of 3
        elif num % 3 == 0:
            print("Fizz", end=" ")
        # check if multiple of 5
        elif num % 5 == 0:
            print("Buzz", end=" ")
        # if not multiple of 3 or 5
        else:
            print(num, end=" ")
