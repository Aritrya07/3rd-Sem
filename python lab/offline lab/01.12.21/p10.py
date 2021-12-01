'''
10. Write programs using nested loops to produce the following patterns:
0
2 2
4 4 4
6 6 6 6
8 8 8 8 8
'''

for i in range(0, 9, 2):
	for j in range(0, i+1, 2):
		print(i, end = ' ')
	print()
