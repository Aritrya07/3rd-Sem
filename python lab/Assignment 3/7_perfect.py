# -*- coding: utf-8 -*-
"""
Write a Python function to check whether a number is perfect or not.
"""

def perfect_check(num):
    s = 0
    for i in range (1, num):
        if num % i == 0:
            s = s + i
    if s == num:
        return 1
    else:
        return 0

n = int(input('Enter  number : '))
x = perfect_check(n)
if x == 1:
    print('Perfect number...')
else:
    print('Not a perfect number...')
