# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def permuatation(iter, prefix=(), result=[]):
    result = []
    def _permuatation(iter, prefix=(), result=result):
        if (len(iter) == 0): 
            result.append(prefix)
            return prefix
        
        for i in range(len(iter)):
            _permuatation(iter[:i] + iter[i+1:], prefix + (iter[i],))

        return result
    return _permuatation(iter, prefix)


def combination(iter, r):
    result = []
    def _comb(iter, r, prefix=(), result=result):
        if not prefix:
            iter = tuple(set(iter))
        
        if (len(iter) == 0 or r == 0):
            result.append(prefix)
            return prefix

        for i in range(len(iter) - r + 1):
            _comb(iter[i+1:], r - 1, prefix + (iter[i],))

        return result
    return _comb(iter, r)


def get_all_combinations(l):
    result = []
    
    for i in range(1, len(l) + 1):
        result.extend(combination(l, i))
    
    return result

my_list = list(map(int, input("Enter the list of numbers (sep by space): ").split()))

print("All the possible combinations are: ")
print(*get_all_combinations(my_list), sep='\n', end="\n")

print("All the possible permutations are: ")
print(*permuatation(my_list), sep='\n', end="\n")