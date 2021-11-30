'''
1. A store charges ₹120 per item if you buy less than 10 items. If you buy between 10 and 99 items, the
cost is ₹100 per item. If you buy 100 or more items, the cost is ₹70 per item. Write a program that asks
the user how many items they are buying and prints the total cost.
'''

n = int(input('Enter number of items : '))
if n < 10:
	c = 120
elif n < 100:
	c = 100
else:
	c = 70
print('Cost =', n*c)
