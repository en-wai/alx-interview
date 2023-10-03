#!/usr/bin/python3
"""
0-pascal_triangle
"""

def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Args:
    n (int): The number of rows to generate.

    Returns:
    list of lists: A list of lists representing Pascal's Triangle up to the nth row.
                   Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []  # Return an empty list for n <= 0
    
    # Initialize an empty list to store the triangle
    triangle = []
    
    for i in range(n):
        # Initialize a row with the first element as 1
        row = [1]
        
        # Fill in the row with values based on the previous row
        for j in range(1, i):
            # Calculate the value by summing the two values above it
            value = triangle[i - 1][j - 1] + triangle[i - 1][j]
            row.append(value)
        
        # Add the last element, which is also 1
        if i > 0:
            row.append(1)
        
        # Append the row to the triangle
        triangle.append(row)
    
    return triangle
