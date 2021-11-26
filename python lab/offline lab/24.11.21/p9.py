'''
9. Write a program to take N (N > 20) as an input from the user. Print numbers from 11 to N.
When the number is a multiple of 3, print "Tipsy", when it is a multiple of 7, print "Topsy".
When it is a multiple of both, print "TipsyTopsy".
'''

n = int(input('Enter number >20 : '))
if n>20:
	for i in range (11, n+1):
		print(i, end = ' ')
		if i%3==0:
			print('Tipsy', end = ' ')
		if i%7==0:
			print('Topsy', end = ' ')
		print()
