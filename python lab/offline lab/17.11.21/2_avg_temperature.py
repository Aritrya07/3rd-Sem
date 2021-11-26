'''
Write a program to obtain temperatures of 7 days (Monday, Tuesday ... Sunday) and then
display average temperature of the week.
'''

day = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
temp = []
s = 0
for i in range(7):
    x = float(input('Enter {} temperature (in degree C) : '.format(day[i])))
    temp.append(x)
    s = s + temp[i]
print('Average temperature = {} degree C'.format(s/7))
