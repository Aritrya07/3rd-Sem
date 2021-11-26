# -*- coding: utf-8 -*-
"""
Write a Python function to sum all the numbers in a list.
"""

def list_sum(l, n):
    sum = 0
    for i in range (n):
        sum = sum + l[i]
    return sum

a = []
n = int(input('Enter number of elements : '))
a = list(map(int,input('Enter elements : ').split()))

y = list_sum(a, n)
print('Sum =', y)