def sum_dig(n):
    s=0
    while n:
        r=n%10
        s+=(r*r)
        n//=10
    return s

n=int(input())
som=sum_dig(n)
while som>=10:
    som=sum_dig(som)
if som==1 or som==7:
    print(True)
else:
    print(False)