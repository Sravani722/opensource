def f(a,k):
    k=k%len(a)
    b=a[-k:]+a[:-k]
    return " ".join(map(str,b))
n=int(input())
a=list(map(int,input().split()))
k=int(input())
print(f(a,k))
