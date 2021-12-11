'''
14. Write a Python program using function to find all the narcissistic or armstrong numbers between 1 and
1000.
'''

def digit_count(n):
    cnt = 0
    while n!=0:
        cnt = cnt + 1
        n = n // 10
    return cnt

def isArmstrong(n):
    c = digit_count(n)
    s = 0
    m = n
    while n!=0:
        r = n % 10
        s = s + (r**c)
        n = n // 10
    if s==m:
        return True
    else:
        return False

for i in range(1, 1001):
    if isArmstrong(i):
        print(i, end = ' ')