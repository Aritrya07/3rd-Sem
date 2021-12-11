'''
8. Write a Python program using function to check whether a number is a Pronic Number or Heteromecic
Number or not.
'''

def isPronic(n):
    a, b = 0, 1
    while a*b<=n:
        if a*b==n:
            return True
        a = a + 1
        b = b + 1
    return False

n = int(input('Enter number : '))
if isPronic(n):
    print('{} is pronic number'.format(n))
else:
    print('{} is not pronic number'.format(n))