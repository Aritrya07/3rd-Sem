# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 14:33:06 2021

@author: Aritrya
"""

def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        return 1
    else:
        return 0

a=int(input('Enter upper limit : '))
for i in range(1, a+1):
    x = prime(i)
    y = prime(i+2)
    if x==1 and y==1:
        print(i,'\t',i+2)
