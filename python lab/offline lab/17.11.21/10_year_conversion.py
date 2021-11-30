'''
10. Write a program that asks a user for a number of years, and then prints out the number
of days, hours, minutes, and seconds in that number of years.
'''

y = int(input('Enter number of years : '))
d = y * 365
h = d * 24
m = h * 60
s = m * 60
print('{} year = {} days'.format(y, d))
print('{} year = {} hours'.format(y, h))
print('{} year = {} minutes'.format(y, m))
print('{} year = {} seconds'.format(y, s))
