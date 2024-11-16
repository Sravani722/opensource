def f(n,m):
    r=[0]*n
    c=[0]*n
    for i in range(n):
        for j in range(n):
            r[i]+=m[i][j]
            c[j]+=m[i][j]
    ma=[]
    for i in range(n):
        ma.append(r[i]+c[i])
    return ma
n=int(input())
m=[]
for _ in range(n):
    r=list(map(int,input().split()))
    m.append(r)
print(" ".join(map(str,f(n,m))))
