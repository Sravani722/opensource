def f(a):
    m=0
    c=0
    for i in a:
        c+=i
        m=max(m,c)
    return m
n=int(input())
a=list(map(int,input().split()))
print(f(a))
