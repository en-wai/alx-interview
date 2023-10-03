#!/usr/bin/python3
"""
0-pascal_triangle
"""


def generate_pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Args:
    n (int): The number of rows to generate Pascal's Triangle for.

    Returns:
    list of lists: A list of lists representing Pascal's Triangle up to the nth row.
                   Returns an empty list if n <= 0.
    """
    pascal_triangle = []
    
    if n <= 0:
        return pascal_triangle
    
    pascal_triangle = [[1]]

    for i in range(1, n):
        temp_row = [1]
        prev_row = pascal_triangle[i - 1]
        
        for j in range(len(prev_row) - 1):
            temp_row.append(prev_row[j] + prev_row[j + 1])
        
        temp_row.append(1)
        pascal_triangle.append(temp_row)
    
    return pascal_triangle
