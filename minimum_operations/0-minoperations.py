#!/usr/bin/python3
""" 
main file for testing 
"""

def minOperations(n):
    """
    calculates fewest number of operations
    """
    a = 0
    b = 2
    while n > 1:
        while n % b == 0:
            a += b
            n = n / b
            b += 1
            return a