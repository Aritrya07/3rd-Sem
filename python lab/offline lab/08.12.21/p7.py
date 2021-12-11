'''
7. Write a Python program using function to check whether a number is a Harshad Number or not.
'''

def isHarshad(n):
    m = n
    s = 0
    while n!=0:
        r = n % 10
        s = s + r
        n = n // 10
    if m%s==0:
        return True
    else:
        return False

n = int(input('Enter number : '))
if isHarshad(n):
    print('{} is harshad number'.format(n))
else:
    print('{} is not harshad number'.format(n))