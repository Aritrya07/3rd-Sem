'''
Write a program that reads a number of seconds and prints it in form : mins and seconds,
e.g., 200 seconds are printed as 3 mins and 20 seconds.
'''

s = int(input('Enter time in seconds : '))
m = s // 60
s = s % 60
print('Time : {} minutes {} seconds'.format(m, s))
