#!/usr/bin/python3
"""Script to determine pascal triangle"""


def pascal_triangle(n):
    """return list representing pascal triangle
    """
    triangle = []

    if n <= 0:
        return []
    for i in range(n):
        temp_list = []
        for j in range(i + 1):
            if j == 0 or j == i:
                temp_list.append(1)
            else:
                temp_list .append(triangle[i-1][j-i] + triangle[i-][j])
        triangle.append(temp_list)
        return triangle
