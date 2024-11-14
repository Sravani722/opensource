def f(x,y,z):
    if (x*y)<=1440*z:
        print("YES")
    else:
        print("NO")
x,y,z=map(int,input().split())
f(x,y,z)    
