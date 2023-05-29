n=int(input())
num=abs(n)
rev=0
while num:
    r=num%10
    rev=rev*10+r
    num//=10
if n<0:
    print("-{}".format(rev))
else:
    print(rev)