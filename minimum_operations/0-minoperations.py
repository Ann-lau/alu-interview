#!/usr/bin/python3
"""
main file for testing
"""


def minOperations(n):
    """
    calculates minimum number of operations
    """
    if n <= 1:
        return 0
    Args, evn, Operations = n, 2, 0

    while Args > 1:
        if Args % evn == 0:
            Args = Args / evn
            Operations = Operations + evn
        else:
                evn += 1
    return Operations