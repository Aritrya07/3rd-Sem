'''
3. Write a program to input 3 sides of a triangle and print whether it is an equilateral, scalene or
isosceles triangle.
'''

def equal(a, b):
	if a==b:
		return 1
	else:
		return 0

a, b, c = map(int, input('Enter 3 sides of a triangle : ').split())
x = equal(a, b)
y = equal(b, c)
z = equal(c, a)
if x+y+z==3:
	print('Equilateral triangle')
elif x+y+z==1:
	print('Isosceles triangle')
elif x+y+z==0:
	print('Scalen triangle')
