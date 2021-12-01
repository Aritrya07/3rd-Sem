'''
23a. Write programs to find the sum of the following series:
x - x^2 /2! + x^3 /3! - x^4 /4! + x^5 /5! - x^6 /6! (Input x)
'''

def fact(n):
	if n==0:
		return 1
	else:
		return n * fact(n-1)

s = 0
x = int(input('Enter value of x : '))
for i in range(1, 7):
	z = (x**i) / fact(i)
	if i%2==0:
		s = s - z
	else:
		s = s + z
print(s)
