#!/usr/bin/python3
"""
Module for matrix_divided function.

This module provides a function that divides all elements of a matrix
by a specific number, with proper validation of input.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a number.

    Args:
        matrix (list of lists): A matrix of integers or floats.
        div (int or float): The number to divide the matrix elements by.

    Returns:
        list of lists: A new matrix with the elements divided by div.

    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats.
        TypeError: If the rows of the matrix are not the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is zero.
    """
    # Validate matrix
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(ele, (int, float)) for row in matrix for ele in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Validate that all rows are of the same size
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
  
    # Validate div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Return a new matrix with each element divided by div,
    # rounded to 2 decimal places
    return [[round(ele / div, 2) for ele in row] for row in matrix]
