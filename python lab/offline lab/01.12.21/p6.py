'''
6. Write programs to print the following shapes:(if row=4)
*
* *
*   *
*     *
*   *
* *
*
'''

r = int(input('Enter number of rows : '))
for i in range(1, r+1):
	for j in range(1, i+1):
		if j==1 or j==i:
			print('*', end = ' ')
		else:
			print(' ', end = ' ')
	print()
for i in range(1, r):
	for j in range(i, r):
		if j==i or j==r-1:
			print('*', end = ' ')
		else:
			print(' ', end = ' ')
	print()
