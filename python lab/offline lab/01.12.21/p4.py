'''
4. Write a program to accept the age of n employees and count the number of persons in the
following age group:
(i) 26 - 35
(ii) 36 - 45
(iii) 46 - 55
'''
a = []
c1 = c2 = c3 = 0
n = int(input('Enter value of n : '))
for i in range(n):
	x = int(input('Enter age : '))
	a.append(x)
	if x>=26 and x<=35:
		c1 = c1 + 1
	elif x>=36 and x<=45:
		c2 = c2 + 1
	elif x>= 46 and x<=55:
		c3 = c3 + 1
print('26 - 35 : {} people'.format(c1))
print('36 - 45 : {} people'.format(c2))
print('46 - 55 : {} people'.format(c3))
