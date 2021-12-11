'''
2. Write a Python program using function to classify Abundant, deficient and perfect number (integers)
between 1 to 10,000.
'''

def div(n):
    s = 0
    for i in range(1, n):
        if n%i==0:
            s = s + i
    return s


for i in range(1, 1001):
    s = div(i)
    if s>i:
        print('{} is abundant'.format(i))
    elif s==i:
        print('{} is perfect'.format(i))
    else:
        print('{} is deficient'.format(i))
    