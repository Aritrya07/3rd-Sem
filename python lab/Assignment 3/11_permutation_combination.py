# -*- coding: utf-8 -*-
"""
Write a python program to show the permutation and
combination of a inputted List.
"""

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

def nCr(n, r):
    com = fact(n) / (fact(r) * fact(n - r))
    return com

def nPr(n, r):
    per = fact(n) / fact(n - r)
    return per

n = int(input('Enter the value of n : '))
r = int(input('Enter the value of r : '))
print('Permutation = ', nPr(n, r))
print('Combination = ', nCr(n, r))