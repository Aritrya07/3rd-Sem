# -*- coding: utf-8 -*-
"""
Write a Python function that accepts a string and calculate the number
of upper case letters and lower case letters.
"""

def count(str):
    u, l = 0, 0
    for i in range(0, len(str)):
        if str[i] >= "A" and str[i] <= "Z":
            u = u + 1
        elif str[i] >= 'a' and str[i] <= 'z':
            l = l + 1
    return u, l

a = input('Enter string : ')
x, y = count(a)
print('Lower case =', y, '\tUpper case =', x)