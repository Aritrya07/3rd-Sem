'''
2. Write a program that asks the user for two numbers and prints Close if the numbers are within .001
of each other and Not close otherwise.
'''

a, b = map(float, input('Enter 2 numbers : ').split())
if a-b<0.001 and a-b>=0:
	print('Close')
elif b-a<0.001 and b-a>=0:
	print('Close')
else:
	print('Not Close')
