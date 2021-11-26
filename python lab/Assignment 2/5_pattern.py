# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 14:24:23 2021

@author: Aritrya
"""

n = int(input('Enter number of lines : '))
for i in range (1, n+1):
    for j in range (1, n+1):
        if i == 1 or i == n or j == 1 or j == n:
            print('*', end = '\t')
        else:
            print(' ', end = '\t')
    print()
