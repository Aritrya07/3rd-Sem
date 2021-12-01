'''
1. Given a list of integers, write a program to find those which are palindromes.
'''

def rev(n):
	s = 0
	while n!=0:
		r = n % 10
		s = s * 10 + r
		n = n // 10
	return s

while True:
	n = input('Enter number (Enter q to stop) : ')
	if n=='q' or n=='Q':
		break
	else:
		x = rev(int(n))
		if int(n)==x:
			print('{} is palindrome'.format(n))
		else:
			print('{} is not palinrome'.format(n))
