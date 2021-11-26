'''
4. Write a short program to input a digit and print it in words.
'''

a = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
n = int(input('Enter a digit (0-9) : '))
if n<0 or n>9:
	print('Out of bound...')
else:
	print('{} = {}'.format(n, a[n]))
