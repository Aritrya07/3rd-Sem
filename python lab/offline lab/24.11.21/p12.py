'''
12. Write a short program to print the following series :
(i) 1 4 7 10 .......... 40.
(ii) 1 -4 7 -10 .......... -40
'''

for i in range(1, 41, 3):
	print(i, end = ' ')
print()

i = 1
x = 1
while i<=40:
	if x%2==0:
		print(i*(-1), end = ' ')
	else:
		print(i, end = ' ')
	i = i + 3
	x = x + 1
print()
