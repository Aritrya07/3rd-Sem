# -*- coding: utf-8 -*-
"""
Write a Python function that takes a list and returns a new list with
unique elements of the first list.
"""

def unique(l, n):
    c = 0
    l2 = []
    for i in range (n):
        for j in range (n):
            if l[i] == l[j]:
                c = c + 1
        if c == 1:
            l2.append(l[i])
        c = 0
    return l2

l = []
n = int(input('Enter number of elements : '))
for i in range (n):
    x = int(input('Enter element : '))
    l.append(x)
z = unique(l, n)
print(z)