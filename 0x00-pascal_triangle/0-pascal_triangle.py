#!/usr/bin/python3
"""
Generate Pascal's Triangle up to the nth row.
"""

def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Args:
        n (int): The number of rows to generate Pascal's Triangle.

    Returns:
        list of lists: A list of lists representing Pascal's Triangle up to the nth row.
                       Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for row_number in range(1, n):
        previous_row = triangle[-1]
        new_row = [1]
        
        for i in range(len(previous_row) - 1):
            new_element = previous_row[i] + previous_row[i + 1]
            new_row.append(new_element)
        
        new_row.append(1)
        triangle.append(new_row)

    return triangle
