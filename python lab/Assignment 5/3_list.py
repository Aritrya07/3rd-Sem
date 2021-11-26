# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 14:38:20 2021

@author: Aritrya
"""

def insert(l, a, pos):
    lst = l
    lst.insert(pos, a)
    print(lst)
    lst.pop(pos)

l = []
n = int(input("Enter number of element : "))
for i in range(n):
    x = int(input("Enter element : "))
    l.append(x)
a = int(input("Enter value to insert : "))
for i in range(n+1):
    insert(l, a, i)