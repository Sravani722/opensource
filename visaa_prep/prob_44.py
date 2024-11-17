def f(n):
    s=-1 if n<0 else 1
    n=abs(n)
    a=int(str(n)[::-1])
    a*=s
    if a<-2**31 or a>2**31-1:
        return 0
    return a
n=int(input())
print(f(n))
