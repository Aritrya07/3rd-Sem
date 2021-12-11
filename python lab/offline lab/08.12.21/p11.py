'''
11. Write a Python program using function to check two numbers are Amicable numbers or not.
'''

def div(n):
    s = 0
    for i in range(1, n):
        if n%i==0:
            s = s + i
    return s

x, y = map(int, input('Enter 2 numbers : ').split())
if x==div(y) and y==div(x):
    print('({},{}) is an amicable pair'.format(x, y))
else:
    print('({},{}) is not an amicable pair'.format(x, y))