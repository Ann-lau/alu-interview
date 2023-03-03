#!/usr/bin/python3
"""
calculating square units of water
"""


def rain(walls):
    """units of water retained"""
    quantity = 0
    for i in range(1, len(walls) - 1):
        left = walls[i]
        for j in range(i):
            left = max(left, walls[j])
        right = walls[i]
        for j in range(i + 1, len(walls)):
            right = max(right, walls[j])

        quantity += (min(left, right) - walls[i])

    return quantity
