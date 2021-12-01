'''
20b. Write Python programs to sum the given sequences:
1^2 + 3^2 + 5^2 + ..... + n^2 (Input n)
'''

s = 0
n = int(input('Enter value of n : '))
for i in range(1, n+1, 2):
	x = i**2
	s = s + x
print(s)
