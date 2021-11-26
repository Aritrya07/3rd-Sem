# -*- coding: utf-8 -*-
"""
Write a Python program that accepts a hyphen-separated sequence
of words as input and prints the words in a hyphen-separated sequence
after sorting them alphabetically.
"""
def sort(s):
    x = '-'
    s2 = x.join(sorted(s.split('-')))
    return s2

s1 = input('Enter string : ')
print('The original string is : ' + str(s1))

s2 = sort(s1)
print("The sorted words : " + str(s2))