n=int(input())
num=n
rev=0
while n:
    r=n%10
    rev=rev*10+r
    n//=10
if num==rev:
    print(True)
else:
    print(False)