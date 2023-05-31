n=int(input())
sq=n*n
rev=0
while n:
    r=n%10
    rev=rev*10+r
    n//=10
rev_sq=rev*rev
rsqr=0
while rev_sq:
    rr=rev_sq%10
    rsqr=rsqr*10+rr
    rev_sq//=10
if rsqr==sq:
    print(True)
else:
    print(False)