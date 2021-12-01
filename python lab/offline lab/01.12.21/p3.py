'''
3. Write a Python program to sum the sequence:
1 + 1/1! + 1/2! + 1/3! + ..... + 1/n! (Input n)
'''

def fact(n):
	if n==0:
		return 1
	else:
		return n * fact(n-1)

s = 0
n = int(input('Enter value of n : '))
for i in range(n+1):
	f = fact(i)
	x = 1 / f
	s = s + x
	print('1/{}'.format(f), end = ' ')
print()
print(s)

