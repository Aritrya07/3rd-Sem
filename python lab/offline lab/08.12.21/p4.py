'''
4. Write a Python program using function to display first 10 lucus numbers.
'''

def lucas(a, b, n):
    if n==0:
        return
    else:
        print(a+b, end = ' ')
        lucas(b, a+b, n-1)

lucas(3, -1, 10)
    