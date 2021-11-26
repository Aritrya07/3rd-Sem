"""
7. Given an input list removes the element at index 4 and add it to the 2nd 
position and also, at the end of the list.
"""

l = []
n = int(input('Enter number of elements : '))
if n < 5 :
    print('Number of elements must be atleast 5...')
else :
    for i in range (n):
        x = int(input('Enter value : '))
        l.append(x)
        
    print('Original list :', l)
    
    x = l[4]
    l.pop(4)
    print('After removing the element at index 4 :', l)
    
    l.insert(2, x)
    print('After adding the element to the 2nd index :', l)
    
    l.append(x)
    print('Final list :', l)
