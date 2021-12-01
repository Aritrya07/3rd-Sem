'''
5. Write programs to print the following shapes:(if row=3)
*
* *
* * *
* *
*
'''

r = int(input('Enter number of rows : '))
for i in range(1, r+1):
	for j in range(1, i+1):
		print('*', end = ' ')
	print()
for i in range(1, r):
	for j in range(i, r):
		print('*', end = ' ')
	print()
