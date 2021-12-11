'''
13. Write a Python program using function to display first 10 Fermat numbers.
'''

def isFermat(n):
    i = 0
    while(1):
        r = (2**(2**i)) + 1
        if r==n:
            return True
        elif r>n:
            return False
        i = i + 1

x = i = 0
while x<=10:
    if isFermat(i):
        print(i, end = ' ')
        x = x + 1
    i = i + 1