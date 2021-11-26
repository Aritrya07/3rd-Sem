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
