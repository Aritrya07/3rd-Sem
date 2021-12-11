'''
5. Write a Python program using function to find and print the first 10 happy numbers.
'''

def happy(n):
    s = 0
    for i in range(10):
        while n!=0:
            r = n % 10
            s = s + (r**2)
            n = n // 10
        if s==1:
            return True
        else:
            n = s
            s = 0
    return False

n = 0
i = 1
while n < 10:
    if happy(i):
        print(i, end = ' ')
        n = n + 1
    i = i + 1
        