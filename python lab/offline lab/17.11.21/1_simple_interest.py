'''
Write a program to obtain principal amount, rate of interest and time from user and
compute simple interest.
'''
p, r, t = map(float, input('Enter principal, rate, time : ').split())
si = (p * r * t) / 100
print('Simple interest =', si)
