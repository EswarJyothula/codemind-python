n=int(input())
l=list(map(int,input().split()))
s=sum(l)
print("{:.2f}".format(s/n))