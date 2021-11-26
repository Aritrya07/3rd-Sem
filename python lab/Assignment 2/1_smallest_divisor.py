"""

Write a Python Program to Find the Smallest Divisor of an Integer other
than 1.

"""

n = int(input('Enter number : '))
for i in range (2,n+1):
    if n%i == 0:
        print('Smallest divisor of',n,'is',i)
        break

