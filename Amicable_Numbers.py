n=int(input())
m=int(input())
l1=[]
l2=[]
for i in range(1,n):
    if n%i==0:
        l1.append(i)
for i in range(1,m):
    if m%i==0:
        l2.append(i)
if sum(l1)==m and n==sum(l2):
    print("Amicable")
else:
    print("Not Amicable")