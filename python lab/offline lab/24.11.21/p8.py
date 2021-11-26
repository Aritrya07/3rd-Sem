'''
8. Write a short program to find the average of some numbers entered through the keyboard.
'''

a = []
s = 0
c = 0
while True:
	x = input('Enter numbers : ')
	if x=='q':
		break
	a.append(x)
	c = c + 1

for i in range(c):
	s = s + int(a[i])
print('Average =', s/c)
