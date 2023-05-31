def isfib(n):
    a=0
    b=1
    c=a+b
    if n==a or n==b or n==c:
        print(True)
    while c<n:
        a=b
        b=c
        c=a+b
        if n==c:
            print(True)
            break
    else:
        print("False")
n=int(input())
isfib(n)