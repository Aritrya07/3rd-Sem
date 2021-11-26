# -*- coding: utf-8 -*-
"""
Swap the following two tuples tuple1 = (11, 22) tuple2 = (99, 88)
"""

tuple1 = (11, 22)
tuple2 = (99, 88)
print('Before swap - ')
print('tuple1 :', tuple1, '\ttuple2 :', tuple2)
tuple1, tuple2 = tuple2, tuple1
print('After swap - ')
print('tuple1 :', tuple1, '\ttuple2 :', tuple2)
