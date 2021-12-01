'''
2. Write Python programs to sum the given sequences:
2/9 - 5/13 + 8/17 ...... (print 7 terms)
'''

n, d = 2, 9
s = 0
for i in range(7):
	x = n / d
	print('{}/{}'.format(n, d), end = ' ')
	n = n + 3
	d = d + 4
	s = s + x
print()
print(s)
