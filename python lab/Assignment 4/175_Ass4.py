''' 
             Python Lab
PCC-CS393

ASSIGNMENT-4


_____________________________________________________________________________________________________

1. Implement stack using Python.

Code : 
'''
def push(a,t,n):
    if top==n-1:
        print('Stack overflown...')
    else:
        val=int(input('Enter value : '))
        t+=1
        a.append(val)
    return a,t
def pop(a,t,n):
    if t==-1:
        print('Stack is empty...')
    else:
        d=a[t]
        print('Deleted item =',d)
        a.pop()
        t-=1
    return a,t
def display(a,t):
    if t==-1:
        print('Stack is empty...')
    else:
        for i in range(t+1):
            print(a[i],end='\t')
        print()
arr=[]
top=-1
n=int(input('Enter number of elements : '))
while True:
    print('1.PUSH\n2.POP\n3.DISPLAY\n4.EXIT')
    ch=int(input('Enter yout choice : '))
    if ch==1:
        arr,top=push(arr,top,n)
    elif ch==2:
        arr,top=pop(arr,top,n)
    elif ch==3:
        display(arr,top)
    elif ch==4:
        break
    else:
        print('Wrong choice...')

'''
Output :

Enter number of elements : 5
1.PUSH
2.POP
3.DISPLAY
4.EXIT

Enter yout choice : 1

Enter value : 11
1.PUSH
2.POP
3.DISPLAY
4.EXIT

Enter yout choice : 1

Enter value : 22
1.PUSH
2.POP
3.DISPLAY
4.EXIT

Enter yout choice : 1

Enter value : 33
1.PUSH
2.POP
3.DISPLAY
4.EXIT

Enter yout choice : 3
11	22	33	
1.PUSH
2.POP
3.DISPLAY
4.EXIT

Enter yout choice : 2
Deleted item = 33
1.PUSH
2.POP
3.DISPLAY
4.EXIT

Enter yout choice : 1

Enter value : 44
1.PUSH
2.POP
3.DISPLAY
4.EXIT

Enter yout choice : 1

Enter value : 55
1.PUSH
2.POP
3.DISPLAY
4.EXIT

Enter yout choice : 1

Enter value : 66
1.PUSH
2.POP
3.DISPLAY
4.EXIT

Enter yout choice : 3
11	22	44	55	66	
1.PUSH
2.POP
3.DISPLAY
4.EXIT

Enter yout choice : 1
Stack overflown...
1.PUSH
2.POP
3.DISPLAY
4.EXIT

Enter yout choice : 2
Deleted item = 66
1.PUSH
2.POP
3.DISPLAY
4.EXIT

Enter yout choice : 2
Deleted item = 55
1.PUSH
2.POP
3.DISPLAY
4.EXIT

Enter yout choice : 2
Deleted item = 44
1.PUSH
2.POP
3.DISPLAY
4.EXIT

Enter yout choice : 2
Deleted item = 22
1.PUSH
2.POP
3.DISPLAY
4.EXIT

Enter yout choice : 2
Deleted item = 11
1.PUSH
2.POP
3.DISPLAY
4.EXIT

Enter yout choice : 2
Stack is empty...
1.PUSH
2.POP
3.DISPLAY
4.EXIT

Enter yout choice : 1

Enter yout choice : 3
Stack is empty...
1.PUSH
2.POP
3.DISPLAY
4.EXIT

Enter yout choice : 4

-------------------------------------------------------------------------------------------------------------

2. Reduce a string of lowercase characters in range ascii[‘a’..’z’]by doing a series of operations. 
   In each operation, select a pair of adjacent letters that match, and delete them. Delete as many characters
   as possible using this method and return the resulting string. If the final string is empty, return Empty String.

   Input-aaabccddd, output-abd, input- abba output-empty string.


Code :
'''
s='aaabccddd'
li=[]
for i in range(97,123):
    x=s.count(chr(i))
    li.append(x)
final=[]
count=0    
for x in li:
    if x>0:
        if x%2!=0:
            final.append(chr(count+97))
    count+=1
fstr = ' '.join([str(elem) for elem in final])
print(fstr)
'''
Output :
a b d

-------------------------------------------------------------------------------------------------------------

3. Represent an integer number in Roman.

Code :
'''
def roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    r = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    rn = ''
    i = 0
    while  num > 0:
        for _ in range(num // val[i]):
            rn += r[i]
            num -= val[i]
        i += 1
    return rn

a = int(input('Enter number : '))
x = roman(a)
print(x)
'''
Output :
Enter number : 777
DCCLXXVII

-------------------------------------------------------------------------------------------------------------

4. Find the Twins primes between a range( Twin primes are pairs of prime numbers that have just one number
   between them: 5 and 7, 11 and 13, and 29 and 31).

Code :
'''
def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        return 1
    else:
        return 0

a=int(input('Enter upper limit : '))
for i in range(1, a+1):
    x = prime(i)
    y = prime(i+2)
    if x==1 and y==1:
        print(i,'\t',i+2)
'''
Output :
Enter upper limit : 100
3 	 5
5 	 7
11 	 13
17 	 19
29 	 31
41 	 43
59 	 61
71 	 73

-------------------------------------------------------------------------------------------------------------

5. Find out the palindromic prime numbers between a range.

Code :
'''
def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        return 1
    else:
        return 0

def pal(n):
    m=n
    s=0
    while n!=0:
        r=n%10
        s=s*10+r
        n=n//10
    if s==m:
        return 1
    else:
        return 0

a=int(input('Enter lower limit : '))
b=int(input('Enter upper limit : '))
for i in range(a,b+1):
    x=prime(i)
    if x==1 :
        y=pal(i)
        if y==1:
            print(i,end=' ')
'''
Output :
Enter lower limit : 100

Enter upper limit : 1000
101 131 151 181 191 313 353 373 383 727 757 787 797 919 929 

-------------------------------------------------------------------------------------------------------------
'''