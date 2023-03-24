#!/usr/bin/python3
"""pPrint Pascals triangle"""

def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal’s triangle"""

    n = 5
    for i in range (n):
        # adjust space
        print(' '*(n-i), end='')

        # compute power of 11
        print(' '.join(map(str, str(11**i))))
