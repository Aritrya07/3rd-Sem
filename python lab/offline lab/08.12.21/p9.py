'''
9. Write a Python program using function check whether a number is an Automorphic number or not.
'''

def digit_count(n):
    cnt = 0
    while n!=0:
        cnt = cnt + 1
        n = n // 10
    return cnt

def isAutomorphic(n):
    c = digit_count(n)
    s = n * n
    if s%(10**c)==n:
        return True
    else:
        return False

n = int(input('Enter number : '))
if isAutomorphic(n):
    print('{} is automorphic number'.format(n))
else:
    print('{} is not automorphic number'.format(n))