'''
10. Write a program to input N numbers and then print the second largest number.
'''

a = list(map(int, input('Enter numbers : ').split()))
max1, max2 = 0, 0
for i in range(len(a)):
    if a[i]>max1:
        max1 = a[i]
for i in range(len(a)):
    if a[i]>max2 and a[i]<max1:
        max2 = a[i]
print('2nd largest =', max2)