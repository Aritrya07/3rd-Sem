'''
5. Write a Python program to print every integer between 1 and n divisible by m. Also report whether
the number that is divisible by m is even or odd.
'''

m, n = map(int, input('Enter value of m and n : ').split())
for i in range(1, n+1):
	if i%m==0:
		print('{} is divisible by {}'.format(i, m))
		if i%2==0:
			print(i, 'is even')
		else:
			print(i, 'is odd')

