n=int(input())
for i in range(1,n):
    if n%i==0:
        if i*i==n:
            print(True)
            break
else:
    print(False)