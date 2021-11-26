'''
              Python Lab
PCC-CS393

1. You are given a sequence of number A1, A2,…,AN . For each valid i, the star
 value of the element Ai  is the number of valid indices j<i  such that Aj is 
 divisible by Ai. Calculate the maximum star value of a given sequence.

Code :
'''
cnt, m = 0, 0
a = []
n = int(input('Enter number of elements : '))
print('Enter values : ')
for i in range(n):
    val = int(input())
    a.append(val)
for i in range(n):
    for j in range(i+1,n):
        if a[i]%a[j]==0:
            cnt = cnt + 1
    if cnt>m:
        m = cnt
    cnt = 0
print('Star value  =',m)

'''Output : 

Enter number of elements : 5
Enter values : 

10

5

4

3

2
Star value  = 2


2. A permutation p1,p2...pN of {1,2,...,N} is beautiful if pi&pi+1 is greater 
than 0 for every 1≤i<N . You are given an integer N, and your task is to 
construct a beautiful permutation of length N or determine that it's 
impossible. *a&b denotes the bitwise AND of a and b.

Beautiful permutation of 3 and 5. If N=4 it is not possible
1 3 2
2 3 1 5 4

Code :
'''

from itertools import permutations

def isBeautifulPermutation(arr):
    for x, y in zip(arr[:-1], arr[1:]):
        if (x & y == 0):
            return False
    return True

def printBeautifulPermutation(arr):
    for i in arr:
        if (isBeautifulPermutation(i)):
            print(*i, sep=", ", end="\n")

num_array = list(map(int, input("Enter the space-seperated number sequence: ").split()))
printBeautifulPermutation(permutations(num_array))

'''
Output : 

Enter the space-seperated number sequence: 1 2 3 5
1, 5, 3, 2
2, 3, 1, 5
2, 3, 5, 1
5, 1, 3, 2

'''