def f(a):
    b=a[1:]+[a[0]]
    return " ".join(map(str,b))
n=int(input())
a=list(map(int,input().split()))
print(f(a))
