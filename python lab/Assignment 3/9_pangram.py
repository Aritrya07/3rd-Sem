# -*- coding: utf-8 -*-
"""
Write a Python function to check whether a string is a pangram or not.
"""

import string
  
def pangram_check(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return 0
  
    return 1
      
s = input('Enter string : ')
if(pangram_check(s) == 1):
    print("Pangram...")
else:
    print("Not pangram...")
