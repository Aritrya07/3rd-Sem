def reverse(num):
    s = 0
    while num!=0:
        r = num % 10
        s = s * 10 + r
        num = num // 10
    return s

n = int(input('Enter number : '))
print('Reverse of {} is {}'.format(n, reverse(n)))
