def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
m=int(input())
n=int(input())
c=0
for i in range(m,n+1):
    if i!=1 and isprime(i):
        c+=1
print(c)