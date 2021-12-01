'''
8. Write programs using nested loops to produce the following patterns:
A
A B
A B C
A B C D
A B C D E
A B C D E F
'''
x = ['A', 'B', 'C', 'D', 'E', 'F']
for i in range(6):
	for j in range(i+1):
		print(x[j], end = ' ')
	print()
