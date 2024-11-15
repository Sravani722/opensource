def f(a):
    b=[]
    ls=0
    rs=0
    for i in range(len(a)):
        ls=sum(a[:i])
        rs=sum(a[i+1:])
        b.append(abs(ls-rs))
    return " ".join(map(str,b))
n=int(input())
a=list(map(int,input().split()))
print(f(a))
