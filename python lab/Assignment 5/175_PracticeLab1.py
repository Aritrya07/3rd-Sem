'''
              Python Lab
PCC-CS393

ASSIGNMENT-5

_____________________________________________________________________________________________________

1. Today potatoes price are change day by day. Let a salesman will purchase it on some day
   and sell it on other day. Let us consider for a week price of potato are 100, 200, 300, 80, 30,
   200, 250 meaning is that day1 price 100, day2 price is 200 and so on. You have found out on
   which day salesman will buy and sell the potato so that for a week his profit is maximum.
   In the above case salesman will
   buy on day1 and sell it on day3,
   buy on day 5 and sell it on day 7.
   (consider Number of days may be 2 to 30.)

Code : 
'''
def pro(l, i, n):
    k = j = i
    if i == n-1:
        return
    min = l[i]
    for j in range(i+1, n):
        if min > l[j]:
            min = l[j]
        else:
            break
    max = l[j]
    for k in range(j+1, n):
        if max < l[k]:
            max = l[k]
        else:
            break
    profit = max - min
    print('Profit =',profit)
    pro(l, k, n)
    

l = []
p = []
week = int(input('Enter number of week/weeks : '))
days = week * 7
print('Enter cost of potato : ')
for i in range(days):
    x = int(input())
    l.append(x)
pro(l, 0, days);
'''
Output :
Enter number of week/weeks : 1
Enter cost of potato : 

100

200

300

80

30

200

250
Profit = 200
Profit = 220

-------------------------------------------------------------------------------------------------------------

2. Consider a string contains any characters of length. If two consecutive characters is same
   they are called 2- neighbour, if 3 consecutive characters are same they are called 3-
   neighbour and so on. You have to find out a neighbour of maximum size in length.

Code :
'''
cnt, max = 0, 0
s = input('Enter string : ')
l = len(s)
for i in range(l-1):
    if s[i] == s[i+1]:
        cnt = cnt + 1
    else:
        if cnt > max:
            max = cnt
        cnt = 0
if max > 0:
    print(max+1,'- neighbour')
'''
Output :
Enter string : aaabccd
3 - neighbour

-------------------------------------------------------------------------------------------------------------

3. Insert an element in all position of a list. Example
   Insert 10 in a list [1,2,3] output :[[10,1,2,3],[1,10,2,3],[1,2,10,3],[1,2,3,10]]

Code :
'''
def insert(l, a, pos):
    lst = l
    lst.insert(pos, a)
    print(lst)
    lst.pop(pos)

l = []
n = int(input("Enter number of element : "))
for i in range(n):
    x = int(input("Enter element : "))
    l.append(x)
a = int(input("Enter value to insert : "))
for i in range(n+1):
    insert(l, a, i)
'''
Output :
Enter number of element : 3

Enter element : 1

Enter element : 2

Enter element : 3

Enter value to insert : 10
[10, 1, 2, 3]
[1, 10, 2, 3]
[1, 2, 10, 3]
[1, 2, 3, 10]

-------------------------------------------------------------------------------------------------------------
 '''