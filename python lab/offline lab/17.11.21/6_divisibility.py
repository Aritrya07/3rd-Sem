'''
Write a program to take two numbers and print if the first number is fully divisible by
second number or not.
'''

a, b = map(int, input('Enter 2 numbers : ').split())
if a%b==0:
    print('{0} is fully divisible by {1}...'.format(a, b))
else:
    print('{0} is not fully divisible by {1}...'.format(a, b))
