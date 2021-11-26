'''
6. Write a short program to check whether the square root of a number is prime or not.
'''

def isPrime(num):
	c = 0
	for i in range(1, num+1):
		if num%i==0:
			c = c + 1
	if c==2:
		return True
	else:
		return False

n = int(input('Enter number : '))
s = n ** 0.5
if isPrime(int(s)):
	print('Square root of {} = {} -> prime'.format(n, s))
else:
		print('Square root of {} = {} -> not prime'.format(n, s))
