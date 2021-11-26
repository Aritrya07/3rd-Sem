"""

Write a Python Program to print the Prime Factors of an Integer.

"""

def prime(n):
    c = 0
    for i in range(1,n+1):
        if n % i == 0:
            c = c + 1
    if c == 2:
        return 1
    else:
        return 0

n = int(input('Enter number : '))
print('Prime factors of',n,'are -', end = '\t')
for i in range(1,n+1):
    if n % i == 0:
        x = prime(i)
        if x == 1:
            print(i, end = '\t')

