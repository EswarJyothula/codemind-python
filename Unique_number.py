n=int(input())
l=[]
while n:
    r=n%10
    if r in l:
        print("Not Unique Number")
        break
    l.append(r)
    n//=10
else:
    print("Unique Number")