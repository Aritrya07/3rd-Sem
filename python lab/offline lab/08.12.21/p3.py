'''
3. Write a Python program using function to generate and show all Kaprekar numbers less than 1000.
'''

def digit_count(n):
    cnt = 0
    while n!=0:
        cnt = cnt + 1
        n = n // 10
    return cnt

def iskap(n):
    c = digit_count(n)
    a = (n * n) // (10**c)
    b = (n * n) % (10**c)
    if a+b==n:
        return True
    else:
        return False

for i in range(1, 1001):
    if iskap(i):
        print(i, end = ' ')
print()