def f(m,n):
    if m>n:
        return m-n
    else:
        return 0
t=int(input())
for _ in range(t):
    m,n=map(int,input().split())
    print(f(m,n))
