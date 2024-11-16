def f(m):
    n=len(m)
    for i in range(n):
        for j in range(i+1,n):
            m[i][j],m[j][i]=m[j][i],m[i][j]
n=int(input())
m=[]
for _ in range(n):
    r=list(map(int,input().split()))
    m.append(r)
f(m)
for r in m:
    print(*r)
