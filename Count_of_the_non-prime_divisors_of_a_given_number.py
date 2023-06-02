def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
l=[]
for i in range(1,n+1):
    if n%i==0:
        l.append(i)
for i in l:
    if isprime(i):
        l.remove(i)
print(len(l))