# -*- coding: utf-8 -*-
"""
Write a Python function to find the Max of three numbers.
"""

def max(a, b, c):
    if a > b:
        if a > c:
            max = a
        else:
            max = c
    else:
        if b > c:
            max = b
        else:
            max = c
    return max

a = int(input('Enter 1st number : '))
b = int(input('Enter 2ns number : '))
c = int(input('Enter 3rd number : '))

x = max(a, b, c)
print('Max =',x)
