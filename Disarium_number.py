n=int(input())
num=n
l=len(str(n))
s=0
while n:
    r=r=n%10
    s+=(r**l)
    n//=10
    l-=1
if num==s:
    print(True)
else:
    print(False)