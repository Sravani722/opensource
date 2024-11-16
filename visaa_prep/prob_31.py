def f(a):
    m=0
    c=0
    for i in a:
        if i==0:
            c+=1
            
        else:
            c=0
        m=max(m,c)
    return m
n=int(input())
a=list(map(int,input().split()))
print(f(a))
