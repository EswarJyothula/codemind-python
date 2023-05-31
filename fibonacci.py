def fib(n):
    a=0
    b=1
    c=a+b
    l=[]
    if n==1:
        l.append(a)
    elif n==2:
        l.append(a)
        l.append(b)
    elif n==3:
        l.append(a)
        l.append(b)
        l.append(c)
    else:
        l.extend([0,1,1])
    while len(l)<n:
        a=b
        b=c
        c=a+b
        l.append(c)
    return l
n=int(input())
print(*fib(n))