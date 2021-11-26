'''
11. Write a complete Python program to do the following : (i) read an integer X.
(ii) determine the number of digits n in X.
(iii) form an integer Y that has the number of digits n at ten's place and the most significant digit of X
at one's place.
(iv) Output Y. (For example, if X is equal to 2134, then Y should be 42 as there are 4 digits and the
most significant number is 2).
'''

def digit_count(n):
	c = 0
	while n!=0:
		c = c + 1
		n = n // 10
	return c

x = int(input('Enter number : '))
a = digit_count(x)
b = x // (10 ** (a-1))
y = a * 10 + b
print(y)

