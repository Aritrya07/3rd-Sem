""" 2. Given 2 strings, s1, and s2 return a new string made of the first,
middle and last char each input string. """

s1 = "abcde"
s2 = "vwxyz"
s = s1[0] + s2[0] + s1[len(s1)//2] + s2[len(s2)//2] + s1[-1] + s2[-1]
print(s)
