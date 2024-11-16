def f(n,m,mat):
    r=[0]*n
    c=[0]*m
    for i in range(n):
        for j in range(m):
            if mat[i][j]==0:
                r[i]=1
                c[j]=1
    for i in range(n):
        for j in range(m):
            if r[i] or c[j]:
                mat[i][j]=0
    return mat
n,m=map(int,input().split())
mat=[]
for _ in range(n):
    mat.append(list(map(int,input().split())))
a=f(n,m,mat)
for r in a:
    print(" ".join(map(str,r)))
