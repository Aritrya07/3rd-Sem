# -*- coding: utf-8 -*-
"""
Write a Python function to multiply all the numbers in a list.
"""

def list_pro(l, n):
    pro = 1
    for i in range (n):
        pro = pro * l[i]
    return pro

a = []
n = int(input('Enter number of elements : '))
a = list(map(int,input('Enter elements : ').split()))

y = list_pro(a, n)
print('Product =', y)