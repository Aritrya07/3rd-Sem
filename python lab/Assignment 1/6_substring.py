# -*- coding: utf-8 -*-
"""
Display the two substring separated by space.
"""

str = input('Enter string : ')
s1 = str[:len(str)//2]
s2 = str[len(str)//2:]
print(s1,s2)
