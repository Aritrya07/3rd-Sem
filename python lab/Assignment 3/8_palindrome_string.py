# -*- coding: utf-8 -*-
"""
Write a Python function that checks whether a passed string is
palindrome or not.
"""

def pal(str):
    l = len(str) - 1
    f = 0
    tmp = 1
    while f <= l:
        if not str[f] == str[l]:
            tmp = 0
            break
        else:
            f = f + 1
            l = l - 1
    if tmp == 1:
        print('Palindrome...')
    else:
        print('Not palindrome...')

s = input('Enter string : ')
pal(s)