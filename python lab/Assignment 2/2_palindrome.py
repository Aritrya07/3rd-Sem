"""

Write a Python Program to Check whether a Number is a Palindrome or
not.

"""

n = int(input('Enter number : '))
s = 0
m = n
while n != 0:
    r = n % 10
    s = s * 10 + r
    n = n // 10
if s == m:
    print('palindrome...')
else:
    print('Not palindrome...')
