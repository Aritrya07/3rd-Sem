'''
              Python Lab
PCC-CS393

ASSIGNMENT-2


_____________________________________________________________________________________________________

1. Write a Python Program to Find the Smallest Divisor of an Integer other than 1.

Code : 
'''
n = int(input('Enter number : '))
for i in range (2,n+1):
    if n%i == 0:
        print('Smallest divisor of',n,'is',i)
        break
'''
Output :
Enter number : 125
Smallest divisor of 125 is 5

-------------------------------------------------------------------------------------------------------------

2. Write a Python Program to Check whether a Number is a Palindrome or not.

Code :
'''
n = int(input('Enter number : '))
s = 0
m = n
while n != 0:
    r = n % 10
    s = s * 10 + r
    n = n // 10
if s == m:
    print('palindrome...')
else:
    print('Not palindrome...')
'''
Output :
Enter number : 121
palindrome...

-------------------------------------------------------------------------------------------------------------

3. Write a Python Program to print the Prime Factors of an Integer.

Code :
'''
def prime(n):
    c = 0
    for i in range(1,n+1):
        if n % i == 0:
            c = c + 1
    if c == 2:
        return 1
    else:
        return 0

n = int(input('Enter number : '))
print('Prime factors of',n,'are -', end = '\t')
for i in range(1,n+1):
    if n % i == 0:
        x = prime(i)
        if x == 1:
            print(i, end = '\t')
'''
Output :
Enter number : 210
2	3	5	7	

-------------------------------------------------------------------------------------------------------------

4. Print the following pattern

Code :
'''
n = int(input('Enter number of lines : '))
for i in range(n):
    k = i
    for j in range(i+1):
        print(2**k, end = '\t')
        k = k - 1
    print()
'''
Output :
Enter number of lines : 8
1	
2	1	
4	2	1	
8	4	2	1	
16	8	4	2	1	
32	16	8	4	2	1	
64	32	16	8	4	2	1	
128	64	32	16	8	4	2	1	

-------------------------------------------------------------------------------------------------------------

5. Print the following pattern

Code :
'''
n = int(input('Enter number of lines : '))
for i in range (1, n+1):
    for j in range (1, n+1):
        if i == 1 or i == n or j == 1 or j == n:
            print('*', end = '\t')
        else:
            print(' ', end = '\t')
    print()
'''
Output :
Enter number of lines : 7
*	*	*	*	*	*	*	
*	 	 	 	 	 	*	
*	 	 	 	 	 	*	
*	 	 	 	 	 	*	
*	 	 	 	 	 	*	
*	 	 	 	 	 	*	
*	*	*	*	*	*	*	

-------------------------------------------------------------------------------------------------------------

6. The set of input is given as ages. Then print the status according to the rules
	Age Status
	1-1 in born
	2-10 child
	11-17 young
	18-49 adult
	50-79 old
	&gt;80 very old

Code :
'''
age = int(input('Enter age : '))
if age == 1:
    print('in born')
elif age >= 2 and age <= 10:
    print('child')
elif age >= 11 and age <= 17:
    print('young')
elif age >= 18 and age <= 49:
    print('adult')
elif age >= 50 and age <= 79:
    print('old')
elif age >= 80:
    print('very old')
else:
    print('invalid...')
'''
Output:
Enter age : 66
old

-------------------------------------------------------------------------------------------------------------

7. Convert a decimal number to a number of a given base b.

Code :
'''
n = int(input('Enter number of base 10 : '))
b = int(input('Enter base for conversion : '))
s, i = 0, 0
while n != 0:
    r = n % b
    s = ((10 ** i) * r) + s
    i = i + 1
    n = n // b
print(s)
'''
Output :
Enter number of base 10 : 124

Enter base for conversion : 2
1111100
'''
