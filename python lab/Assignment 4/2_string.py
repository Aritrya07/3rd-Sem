# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 15:47:21 2021

@author: Aritrya
"""

s='aaabccddd'
li=[]
for i in range(97,123):
    x=s.count(chr(i))
    li.append(x)
final=[]
count=0    
for x in li:
    if x>0:
        if x%2!=0:
            final.append(chr(count+97))
    count+=1
fstr = ' '.join([str(elem) for elem in final])
print(fstr)