def f(x,y):
    return (x-y)+1
t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    print(f(x,y))
