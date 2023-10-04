#!/usr/bin/python3
"""
Create Pascal's Triangle function
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
    triangle = []
    
    for row_number in range(n):
        current_row = []
        
        for column_number in range(row_number + 1):
            if column_number == 0 or column_number == row_number:
                element = 1
            else:
                element = triangle[row_number - 1][column_number - 1] + triangle[row_number - 1][column_number]
            
            current_row.append(element)
        
        triangle.append(current_row)
    
    return triangle
