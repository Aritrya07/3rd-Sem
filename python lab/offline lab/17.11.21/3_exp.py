'''
Write a program to obtain x, y, z from user and calculate expression : 4x4 + 3y3 + 9z + 6π
Solution
'''

import math
x, y, z = map(int, input('Enter value of x, y, z : ').split())
r = (4 * (x**4)) + (3 * (y**3)) + (9 * z) + (6 * math.pi)
print('Result =', r)
