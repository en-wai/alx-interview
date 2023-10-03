#!/usr/bin/python3
"""
0-pascal_triangle
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
    result = []  # Initialize the result as an empty list

    if n <= 0:
        return result  # Return an empty list for n <= 0

    result = [[1]]  # Initialize the result with the first row [1]

    for i in range(1, n):
        temp_row = [1]  # Initialize a new row with the first element as 1

        for j in range(len(result[i - 1]) - 1):
            prev_row = result[i - 1]  # Get the previous row for calculations
            temp_row.append(prev_row[j] + prev_row[j + 1])  # Calculate and append the next value

        temp_row.append(1)  # Add the last element, which is also 1
        result.append(temp_row)  # Append the new row to the result

    return result
