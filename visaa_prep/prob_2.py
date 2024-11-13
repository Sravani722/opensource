def f(x,y,z):
    if x+y <=z:
        print(2)
    elif x<=z:
        print(1)
    else:
        print(0)
x,y,z=map(int,input().split())
f(x,y,z)
