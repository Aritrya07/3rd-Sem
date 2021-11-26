'''              Python Lab
PCC-CS393

ASSIGNMENT-3

_____________________________________________________________________________________________________

1. Write a Python function to find the Max of three numbers.

Code : 
'''
def max(a, b, c):
    if a > b:
        if a > c:
            max = a
        else:
            max = c
    else:
        if b > c:
            max = b
        else:
            max = c
    return max

a = int(input('Enter 1st number : '))
b = int(input('Enter 2ns number : '))
c = int(input('Enter 3rd number : '))

x = max(a, b, c)
print('Max =',x)
'''
Output :
Enter 1st number : 12

Enter 2ns number : 22

Enter 3rd number : 10
Max = 22
-------------------------------------------------------------------------------------------------------------

2. Write a Python function to sum all the numbers in a list.

Code :
'''
def list_sum(l, n):
    sum = 0
    for i in range (n):
        sum = sum + l[i]
    return sum

a = []
n = int(input('Enter number of elements : '))
a = list(map(int,input('Enter elements : ').split()))

y = list_sum(a, n)
print('Sum =', y)
'''
Output :
Enter number of elements : 5

Enter elements : 4 23 1 5 7
Sum = 40

-------------------------------------------------------------------------------------------------------------

3. Write a Python function to multiply all the numbers in a list.

Code :
'''
def list_pro(l, n):
    pro = 1
    for i in range (n):
        pro = pro * l[i]
    return pro

a = []
n = int(input('Enter number of elements : '))
a = list(map(int,input('Enter elements : ').split()))

y = list_pro(a, n)
print('Product =', y)
'''
Output :
Enter number of elements : 4

Enter elements : 5 7 3 1
Product = 105

-------------------------------------------------------------------------------------------------------------

4. Write a Python function to calculate the factorial of a number (a non-
negative integer). The function accepts the number as an argument.

Code :
'''
def fact(n):
    if(n == 0):
        return 1
    else:
        return n * fact(n - 1)

a = int(input('Enter number : '))
x = fact(a)
print('Factorial =', x)
'''
Output :
Enter number : 6
Factorial = 720

-------------------------------------------------------------------------------------------------------------

5. Write a Python function that accepts a string and calculate the number
of upper case letters and lower case letters.

Code :
'''
def count(str):
    u, l = 0, 0
    for i in range(0, len(str)):
        if str[i] >= "A" and str[i] <= "Z":
            u = u + 1
        elif str[i] >= 'a' and str[i] <= 'z':
            l = l + 1
    return u, l

a = input('Enter string : ')
x, y = count(a)
print('Lower case =', y, '\tUpper case =', x)
'''
Output :
Enter string : AriTrYa sEnaPAtI
Lower case = 8 	Upper case = 7

-------------------------------------------------------------------------------------------------------------

6. Write a Python function that takes a list and returns a new list with
unique elements of the first list.

Code :
'''
def unique(l, n):
    c = 0
    l2 = []
    for i in range (n):
        for j in range (n):
            if l[i] == l[j]:
                c = c + 1
        if c == 1:
            l2.append(l[i])
        c = 0
    return l2

l = []
n = int(input('Enter number of elements : '))
for i in range (n):
    x = int(input('Enter element : '))
    l.append(x)
z = unique(l, n)
print(z)
'''
Output:
Enter number of elements : 9

Enter element : 1

Enter element : 2

Enter element : 3

Enter element : 2

Enter element : 2

Enter element : 4

Enter element : 4

Enter element : 5

Enter element : 6
[1, 3, 5, 6]

-------------------------------------------------------------------------------------------------------------

7. Write a Python function to check whether a number is perfect or not.

Code :
'''
def perfect_check(num):
    s = 0
    for i in range (1, num):
        if num % i == 0:
            s = s + i
    if s == num:
        return 1
    else:
        return 0

n = int(input('Enter  number : '))
x = perfect_check(n)
if x == 1:
    print('Perfect number...')
else:
    print('Not a perfect number...')
'''
Output :
Enter  number : 496
Perfect number...

-------------------------------------------------------------------------------------------------------------

8. Write a Python function that checks whether a passed string is
palindrome or not.

Code :
'''
def pal(str):
    l = len(str) - 1
    f = 0
    tmp = 1
    while f <= l:
        if not str[f] == str[l]:
            tmp = 0
            break
        else:
            f = f + 1
            l = l - 1
    if tmp == 1:
        print('Palindrome...')
    else:
        print('Not palindrome...')

s = input('Enter string : ')
pal(s)
'''
Output : 
Enter string : MaDaM
Palindrome...

-------------------------------------------------------------------------------------------------------------

9. Write a Python function to check whether a string is a pangram or not.

Code :
'''
import string
  
def pangram_check(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return 0
  
    return 1
      
s = input('Enter string : ')
if(pangram_check(s) == 1):
    print("Pangram...")
else:
    print("Not pangram...")
'''
Output :
Enter string : The quick brown fox jumps over the lazy dog
Pangram...

-------------------------------------------------------------------------------------------------------------

10. Write a Python program that accepts a hyphen-separated sequence
of words as input and prints the words in a hyphen-separated sequence
after sorting them alphabetically. Go to the editor

Code :
'''
def sort(s):
    x = '-'
    s2 = x.join(sorted(s.split('-')))
    return s2

s1 = input('Enter string : ')
print('The original string is : ' + str(s1))

s2 = sort(s1)
print("The sorted words : " + str(s2))
'''
Output :
Enter string : green-red-yellow-black-white
The original string is : green-red-yellow-black-white
The sorted words : black-green-red-white-yellow
-------------------------------------------------------------------------------------------------------------

11. Write a python program to show the permutation and
combination of a inputted List.

Code :
'''
def permuatation(iter, prefix=(), result=[]):
    result = []
    def _permuatation(iter, prefix=(), result=result):
        if (len(iter) == 0): 
            result.append(prefix)
            return prefix
        
        for i in range(len(iter)):
            _permuatation(iter[:i] + iter[i+1:], prefix + (iter[i],))

        return result
    return _permuatation(iter, prefix)


def combination(iter, r):
    result = []
    def _comb(iter, r, prefix=(), result=result):
        if not prefix:
            iter = tuple(set(iter))
        
        if (len(iter) == 0 or r == 0):
            result.append(prefix)
            return prefix

        for i in range(len(iter) - r + 1):
            _comb(iter[i+1:], r - 1, prefix + (iter[i],))

        return result
    return _comb(iter, r)


def get_all_combinations(l):
    result = []
    
    for i in range(1, len(l) + 1):
        result.extend(combination(l, i))
    
    return result

my_list = list(map(int, input("Enter the list of numbers (sep by space): ").split()))

print("All the possible combinations are: ")
print(*get_all_combinations(my_list), sep='\n', end="\n")

print("All the possible permutations are: ")
print(*permuatation(my_list), sep='\n', end="\n")
'''
Output :
Enter the list of numbers (sep by space): 11 22 33 44
All the possible combinations are: 
(33,)
(11,)
(44,)
(22,)
(33, 11)
(33, 44)
(33, 22)
(11, 44)
(11, 22)
(44, 22)
(33, 11, 44)
(33, 11, 22)
(33, 44, 22)
(11, 44, 22)
(33, 11, 44, 22)
All the possible permutations are: 
(11, 22, 33, 44)
(11, 22, 44, 33)
(11, 33, 22, 44)
(11, 33, 44, 22)
(11, 44, 22, 33)
(11, 44, 33, 22)
(22, 11, 33, 44)
(22, 11, 44, 33)
(22, 33, 11, 44)
(22, 33, 44, 11)
(22, 44, 11, 33)
(22, 44, 33, 11)
(33, 11, 22, 44)
(33, 11, 44, 22)
(33, 22, 11, 44)
(33, 22, 44, 11)
(33, 44, 11, 22)
(33, 44, 22, 11)
(44, 11, 22, 33)
(44, 11, 33, 22)
(44, 22, 11, 33)
(44, 22, 33, 11)
(44, 33, 11, 22)
(44, 33, 22, 11)
-------------------------------------------------------------------------------------------------------------
'''
