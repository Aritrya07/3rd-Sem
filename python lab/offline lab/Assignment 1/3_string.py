# -*- coding: utf-8 -*-
"""
3. Given 2 strings, s1 and s2, create a new string by 
appending s2 in the middle of s1

"""

str1 = input("Enter 1st string : ")
str2 = input("Enter 2nd string : ")
print(str1[:len(str1)//2] + str2 + str1[len(str1)//2:])
