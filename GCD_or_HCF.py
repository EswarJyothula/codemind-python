m,n=map(int,input().split())
i=m
while 1:
    if m%i==0 and n%i==0:
        print(i)
        break
    i-=1