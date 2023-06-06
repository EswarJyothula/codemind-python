n=int(input())
l=list(map(int,input().split()))
c=int(input())
for i in l:
    if i==c:
        print(True)
        break
else:
    print(False)