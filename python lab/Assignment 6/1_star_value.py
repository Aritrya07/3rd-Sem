# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 21:16:10 2021

@author: Aritrya
"""
cnt, m = 0, 0
a = []
n = int(input('Enter number of elements : '))
print('Enter values : ')
for i in range(n):
    val = int(input())
    a.append(val)
for i in range(n):
    for j in range(i+1,n):
        if a[i]%a[j]==0:
            cnt = cnt + 1
    if cnt>m:
        m = cnt
    cnt = 0
print('Star value  =',m)