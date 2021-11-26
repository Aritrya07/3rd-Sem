'''
              Python Lab
PCC-CS393

ASSIGNMENT-1

Write single python program for all problem of Assignment1. Save it as rollno_Ass1.py and submit.

_____________________________________________________________________________________________________
'''
'''
1. Given a string of length greater than 2, return a string except 1st and last characters.

Code : 
'''
s = input('Enter string : ')
l = len(s)
if l>2 :
    s1 = s[1:l-1]
    print(s1)
else :
    print('String is too short...')

'''
Output :
Enter string : Aritrya
ritry

-------------------------------------------------------------------------------------------------------------

2. Given 2 strings, s1, and s2 return a new string made of the first, middle and last char each input string.

Code :
'''
s1 = "abcde"
s2 = "vwxyz"
s = s1[0] + s2[0] + s1[len(s1)//2] + s2[len(s2)//2] + s1[-1] + s2[-1]
print(s)
'''
Output :
avcxez

-------------------------------------------------------------------------------------------------------------

3. Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1

Code :
'''
str1 = input("Enter 1st string : ")
str2 = input("Enter 2nd string : ")
print(str1[:len(str1)//2] + str2 + str1[len(str1)//2:])
'''
Output :
Enter 1st string : abcd

Enter 2nd string : xyz
abxyzcd

-------------------------------------------------------------------------------------------------------------

4. Find all occurrences of “India” in given string ignoring the case.

Code :
'''
str1="i live india and INDIA is a great country"
str2=str1.lower()
print(str2.count("india"))
'''
Output :
2

-------------------------------------------------------------------------------------------------------------

5. Find the last position of a substring “Emma” in a given string.

Code :
'''
str1 = input('Enter string : ')
x=str1.rfind("Emma")
print(x)
'''
Output :
Enter string : Good morning Emma, How are you?
13

-------------------------------------------------------------------------------------------------------------

6. Display the two substring separated by space.

Code :
'''
str = input('Enter string : ')
s1 = str[:len(str)//2]
s2 = str[len(str)//2:]
print(s1,s2)
'''
Output:
Enter string : pqrs
pq rs

-------------------------------------------------------------------------------------------------------------

7. Given an input list removes the element at index 4 and add it to the 2nd position and also, at the end of the list.

Code :
'''
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
'''
Output :
Enter number of elements : 8

Enter value : 11

Enter value : 22

Enter value : 33

Enter value : 44

Enter value : 55

Enter value : 66

Enter value : 77

Enter value : 88
Original list : [11, 22, 33, 44, 55, 66, 77, 88]
After removing the element at index 4 : [11, 22, 33, 44, 66, 77, 88]
After adding the element to the 2nd index : [11, 22, 55, 33, 44, 66, 77, 88]
Final list : [11, 22, 55, 33, 44, 66, 77, 88, 55]

-------------------------------------------------------------------------------------------------------------

8. Reverse the following tuple aTuple = (10, 20, 30, 40, 50)

Output :
'''
aTuple = (10, 20, 30, 40, 50)
aTuple = aTuple[::-1]
print(aTuple)
'''
Output : 
(50, 40, 30, 20, 10)

-------------------------------------------------------------------------------------------------------------

9. Access value 20 from the following tuple aTuple = ("Orange", [10, 20, 30], (5, 15, 25))

Code :
'''
aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
print(aTuple[1][1])
'''
Output :
20

-------------------------------------------------------------------------------------------------------------

10. Unpack the following tuple into 4 variables aTuple = (10, 20, 30, 40)

Code :
'''
aTuple = (10, 20, 30, 40)
a, b, c, d = aTuple
print(a)
print(b)
print(c)
print(d)
'''
Output :
10
20
30
40

-------------------------------------------------------------------------------------------------------------

11. Swap the following two tuples tuple1 = (11, 22) tuple2 = (99, 88)

Code :
'''
tuple1 = (11, 22)
tuple2 = (99, 88)
print('Before swap - ')
print('tuple1 :', tuple1, '\ttuple2 :', tuple2)
tuple1, tuple2 = tuple2, tuple1
print('After swap - ')
print('tuple1 :', tuple1, '\ttuple2 :', tuple2)
'''
Output :
Before swap - 
tuple1 : (11, 22) 	tuple2 : (99, 88)
After swap - 
tuple1 : (99, 88) 	tuple2 : (11, 22)

-------------------------------------------------------------------------------------------------------------

12. Copy element 44 and 55 from the following tuple into a new tuple tuple1 = (11, 22, 33, 44, 55, 66)

Code : 
'''
tuple1 = (11, 22, 33, 44, 55, 66)
tuple2 = tuple1[3:-1]
print(tuple2)
'''
Output :
(44, 55)

-------------------------------------------------------------------------------------------------------------

13. Modify the first item (22) of a list inside a following tuple to 222 tuple1 = (11, [22, 33], 44, 55)

Code :
'''
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 222
print(tuple1)
'''
Output:
(11, [222, 33], 44, 55)

-------------------------------------------------------------------------------------------------------------

14. Below are the two lists convert it into the dictionary keys = ['Ten', 'Twenty', 'Thirty'] values = [10, 20, 30]

Code :
'''
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
sampleDict = dict(zip(keys, values))
print(sampleDict)
'''
Output:
{'Ten': 10, 'Twenty': 20, 'Thirty': 30}

-------------------------------------------------------------------------------------------------------------
15. Merge following two Python dictionaries into one dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30} dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

Code :
'''
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3 = {**dict1, **dict2}
print(dict3)
'''
Output:
{'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

-------------------------------------------------------------------------------------------------------------
16. Check if a value 200 exists in a dictionary sampleDict = {'a': 100, 'b': 200, 'c': 300}

Code :
'''
sampleDict = {'a': 100, 'b': 200, 'c': 300}
print(200 in sampleDict.values())
'''
Output:
True

-------------------------------------------------------------------------------------------------------------
17. Rename key city to location in the following dictionary 
    sampleDict = { "name": "Kelly",  "age":25,  "salary": 8000,  "city": "New york"}

Code :
'''
sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
sampleDict['location'] = sampleDict.pop('city')
print(sampleDict)
'''
Output:
{'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}

-------------------------------------------------------------------------------------------------------------
18. Get the key corresponding to the minimum value from the following dictionary
    sampleDict = {  'Physics': 82,  'Math': 65,  'history': 75}

Code :
'''
sampleDict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
print(min(sampleDict, key=sampleDict.get))
'''
Output:
Math

-------------------------------------------------------------------------------------------------------------
19. Given a Python dictionary, Change Brad’s salary to 8500
    sampleDict = { 'emp1': {'name': 'Jhon', 'salary': 7500}, 'emp2': {'name': 'Emma', 'salary': 8000},  'emp3': {'name': 'Brad', 'salary': 6500}}
 
Code :
'''
sampleDict = { 'emp1': {'name': 'Jhon', 'salary': 7500}, 'emp2': {'name': 'Emma', 'salary': 8000},  'emp3': {'name': 'Brad', 'salary': 6500}}
sampleDict['emp3']['salary'] = 8500
print(sampleDict)
'''
Output:
{'emp1': {'name': 'Jhon', 'salary': 7500}, 'emp2': {'name': 'Emma', 'salary': 8000}, 'emp3': {'name': 'Brad', 'salary': 8500}}

-------------------------------------------------------------------------------------------------------------
'''
