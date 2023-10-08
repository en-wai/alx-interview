#!/usr/bin/python3
"""A script to determine pascal's triangle for any number"""


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

            # return (trianlgle if n <= 0)
            if n <= 0:
                return triangle
            for row_no in range(n):
                temp_list = []

                for col_no in range(row_no+1):
                    if col_no == 0 or col_no == row_no:
                        temp_list.append(1)
                    else:
                        temp_list.append(triangle[row_no -1][col_no -1] + triangle[row_no-1][col_no])
                triangle.append(temp_list)
            # print(triangle)
            return triangle
