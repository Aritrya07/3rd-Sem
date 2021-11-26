# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 19:17:48 2021

@author: Aritrya
"""

'''Consider a string contains any characters of length. If two consecutive
   characters is same they are called 2 - neighbour, if 3 consecutive
   characters are same they are called 3 - neighbour and so on.
   You have to find out a neighbour of maximum size in length.'''

cnt, max = 0, 0
s = input('Enter string : ')
l = len(s)
for i in range(l-1):
    if s[i] == s[i+1]:
        cnt = cnt + 1
    else:
        if cnt > max:
            max = cnt
        cnt = 0
if max > 0:
    print(max+1,'- neighbour')