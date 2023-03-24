#!/usr/bin/python3
"""pPrint Pascals triangle"""

from math import factorial

def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal’s triangle"""
    if n <= 0:
        return[]
    
    n = 5
    for i in range(n):
        for j in range(n-i+1)

        #for left spacing
        print(end=" ")

    for j in range(i+1):

        #nCr = n!/((n-r)!*r!)
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
