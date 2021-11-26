# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 20:15:50 2021

@author: Aritrya
"""

def pro(l, i, n):
    k = j = i
    if i == n-1:
        return
    min = l[i]
    for j in range(i+1, n):
        if min > l[j]:
            min = l[j]
        else:
            break
    max = l[j]
    for k in range(j+1, n):
        if max < l[k]:
            max = l[k]
        else:
            break
    profit = max - min
    print('Profit =',profit)
    pro(l, k, n)
    

l = []
p = []
week = int(input('Enter number of week/weeks : '))
days = week * 7
print('Enter cost of potato : ')
for i in range(days):
    x = int(input())
    l.append(x)
pro(l, 0, days);


                        