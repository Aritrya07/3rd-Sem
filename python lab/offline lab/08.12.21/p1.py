'''
1. Write a Python program using function to check whether a given number is an ugly number.
'''

def ugly(n, i):
    if n==0:
        return
    elif i==1 or i%2==0 or i%3==0 or i%5==0:
        print(i, end = ' ')
        ugly(n-1, i+1)
    else:
        ugly(n, i+1)

ugly(10, 1)
print()