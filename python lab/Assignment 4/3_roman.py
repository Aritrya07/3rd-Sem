# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 14:47:29 2021

@author: Aritrya
"""


def roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    r = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    rn = ''
    i = 0
    while  num > 0:
        for _ in range(num // val[i]):
            rn += r[i]
            num -= val[i]
        i += 1
    return rn

a = int(input('Enter number : '))
x = roman(a)
print(x)