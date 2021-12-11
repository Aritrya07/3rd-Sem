'''
12. Write a Python program using function to check if a given number is circular prime or not.
'''

def digit_count(n):
    cnt = 0
    while n!=0:
        cnt = cnt + 1
        n = n // 10
    return cnt

def isPrime(n):
    c = 0
    for i in range(1, n+1):
        if n%i==0:
            c = c + 1
    if c==2:
        return True
    else:
        return False

p = 0
n = int(input('Enter number : '))
c = digit_count(n)
for i in range(c):
    a = n % 10
    b = n // 10
    n = (a * (10**(c - 1))) + b
    if isPrime(n):
        p = p + 1
    else:
        break
if p==c:
    print('Circular prime')
else:
    print('Not circular prime')