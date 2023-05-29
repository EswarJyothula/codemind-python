n=int(input())
m=int(input())
l1=[]
l2=[]
for i in range(1,n):
    if n%i==0:
        l1.append(i)
for j in range(1,m):
    if m%j==0:
        l2.append(j)
if sum(l1)==m and sum(l2)==n:
    print("Amicable")
else:
    print("Not Amicable")