'''
9. Write programs using nested loops to produce the following patterns:
A
B B
C C C
D D D D
E E E E E
'''

x = ['A', 'B', 'C', 'D', 'E']
for i in range(5):
	for j in range(i+1):
		print(x[i], end = ' ')
	print()
