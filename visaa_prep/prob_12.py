def f(n,x,y):
    if y//x<=n and y%x==0:
        return ("YES")
    else:
        return ("NO")
n,x,y=map(int,input().split())
print(f(n,x,y))
