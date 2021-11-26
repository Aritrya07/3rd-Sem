# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 14:31:24 2021
1-1 in born
2-10 child
11-17 young
18-49 adult
50-79 old
&gt;80 very old
@author: Aritrya
"""

age = int(input('Enter age : '))
if age == 1:
    print('in born')
elif age >= 2 and age <= 10:
    print('child')
elif age >= 11 and age <= 17:
    print('young')
elif age >= 18 and age <= 49:
    print('adult')
elif age >= 50 and age <= 79:
    print('old')
elif age >= 80:
    print('very old')
else:
    print('invalid...')