#!/usr/bin/python3
"""
This module defines a function to generate Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the nth row.

    Args:
        n (int): The number of rows in Pascal's Triangle to generate.

    Returns:
        list of lists: A list of lists where each list represents a row in Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Start with the first row

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # Start with the first element in the row
        
        # Generate the middle elements
        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j - 1] + prev_row[j])
        
        new_row.append(1)  # End with the last element in the row
        triangle.append(new_row)
    
    return triangle
