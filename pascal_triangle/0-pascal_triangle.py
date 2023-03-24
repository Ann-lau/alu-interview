#!/usr/bin/python3
"""pPrint Pascals triangle"""

def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal’s triangle"""

    n = 5

    for i in range(1, n+1):
        for j in range(0, n-i+1):
            print(' ', end='')

            # first element is always 1
            c = 1
            for j in range(1, i+1):

                #first value in a line is always 1
                print(' ', C, sep='', end='')

                #using binomial coefficient
                C = C * (i - j) // j
        print(pascal_triangle)
