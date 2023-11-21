#!/usr/bin/python3
"""Matrix Rotation Module"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix (NxN) 90 degrees clockwise.

    Args:
    - matrix (list[list[int]]): The input matrix to be rotated.

    Returns:
    - None: The function modifies the input matrix in-place.
    """
    n = len(matrix)  # Get the size of the matrix

    # Create a new matrix to store the rotated values
    rotated_matrix = []
    for row in range(n):
        new_row = []
        for col in range(n - 1, -1, -1):
            new_row.append(matrix[col][row])
        rotated_matrix.append(new_row)

    # Update the original matrix with the rotated values
    for i in range(n):
        for j in range(n):
            matrix[i][j] = rotated_matrix[i][j]

# Example usage:
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# rotate_2d_matrix(matrix)
# print(matrix)
