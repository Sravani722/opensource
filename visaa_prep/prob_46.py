def f(n,k):
    a=1<<(k-1)
    if n&a:
        print("true")
    else:
        print("false")
n=int(input())
k=int(input())
f(n,k)
