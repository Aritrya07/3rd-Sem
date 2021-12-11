'''
6. Write a Python program using function to check whether a given number is a Disarium number or
not.
'''

def digit_count(n):
    cnt = 0
    while n!=0:
        cnt = cnt + 1
        n = n // 10
    return cnt

def disarium(n):
    m = n
    s = 0
    c = digit_count(n)
    while n!=0:
        r = n % 10
        s = s + (r**c)
        c = c - 1
        n = n // 10
    if s==m:
        return True
    else:
        return False

n = int(input('Enter number : '))
if disarium(n):
    print(n, 'is Disarium number')
else:
    print(n, 'is not Disarium number')