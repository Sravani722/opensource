def f(x,n):
    return (x//10)*n
t=int(input())
for _ in range(t):
    x,n=map(int,input().split())
    print(f(x,n))
