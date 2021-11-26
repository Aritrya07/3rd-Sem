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
