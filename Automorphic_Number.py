n=int(input())
l=len(str(n))
sq=n*n
d=sq%pow(10,l)
if d==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")