'''
Write a program to take two inputs for day, month and then calculate which day of the
year, the given date is.
'''

def isLeapYear(year):
    if year%4==0 and year%100!=0 or year%400==0:
        return True
    else:
        return False

days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
i, s = 0, 0
d, m, y = map(int, input('Enter date dd/mm/yyyy : ').split('/'))
if(isLeapYear(y)):
    days[2] = days[2] + 1
try:
    if d > days[m] or m < 1 and m > 12:
        print('Invalid date...')
    else:
        while i < m:
            s = s + days[i]
            i = i + 1
        s = s + d
        print('{}/{}/{} is {}th day of the year'.format(d, m, y, s))
except:
    print('Invalid date...')
