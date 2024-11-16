def f(m,a):
    n1=[]
    n2=[]
    for i in a:
        if i%m==0:
            n1.append(i)
        else:
            n2.append(i)
    return sum(n1)-sum(n2)
n,m=map(int,input().split())
a=list(map(int,input().split()))
print(f(m,a))
