# -*- coding: utf-8 -*-
"""

Convert a decimal number to a number of a given base b.

"""

n = int(input('Enter number of base 10 : '))
b = int(input('Enter base for conversion : '))
s, i = 0, 0
while n != 0:
    r = n % b
    s = ((10 ** i) * r) + s
    i = i + 1
    n = n // b
print(s)
