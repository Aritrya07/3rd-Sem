""" 1. Given a string of length greater than 2, return a string except 1st 
and last characters. """

s = input('Enter string : ')
l = len(s)
if l>2 :
    s1 = s[1:l-1]
    print(s1)
else :
    print('String is too short...')