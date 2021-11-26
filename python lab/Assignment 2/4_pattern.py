# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 14:19:16 2021

@author: Aritrya
"""

n = int(input('Enter number of lines : '))
for i in range(n):
    k = i
    for j in range(i+1):
        print(2**k, end = '\t')
        k = k - 1
    print()
