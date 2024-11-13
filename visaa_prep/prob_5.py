def f(a,b,c,x):
    if ((a+b) or (b+c) or (c+a))>=x:
        print("YES")
    else:
        print("NO")
a,b,c,x=map(int,input().split())
f(a,b,c,x)
