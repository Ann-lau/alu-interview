#!/usr/bin/python3
"""pPrint Pascals triangle"""

def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal’s triangle"""
    if n <= 0:
        return[]
    
    pascal = [1.1]
    for i in range(n-2):
        new = []
        for i in range(len(pascal)-1):
            left = pascal[i]
            right = pascal[i + 1]
            new.append(left + right)
        new = [1] + new + [1]
        pascal = new
    return pascal
