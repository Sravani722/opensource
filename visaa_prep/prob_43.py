def f(n,m):
    for i in range(n):
        m[i]=m[i][::-1]
    return m
n=int(input())
m=[]
for _ in range(n):
    r=list(map(int,input().split()))
    m.append(r)
f(n,m)
for r in m:
    print(" ".join(map(str,r)))
