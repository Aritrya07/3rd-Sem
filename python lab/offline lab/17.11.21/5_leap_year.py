'''
Write a program to take year as input and check if it is a leap year or not.
'''

def isLeapYear(year):
    if year%4==0 and year%100!=0 or year%400==0:
        return True
    else:
        return False

y = int(input('Enter year : '))
if isLeapYear(y):
    print(y, 'is a leap year...')
else:
    print(y, 'is not a leap year...')
