'''
10. Write a Python program using function to check whether a number is a Duck Number or not.
'''

def isDigit(a):
    if a>='0' and a<='9':
        return True
    else:
        return False

def check_duck(num):
    n = len(num)
    if isDigit(num[0]):
        for i in range(1, n):
            if isDigit(num[i]):
                if num[i]=='0':
                    return True
            else:
                return False
        return False
    else:
        return False

x = input('Enter number : ')
if check_duck(x):
	print('It is a duck number')
else :
	print('It is not a duck number')
