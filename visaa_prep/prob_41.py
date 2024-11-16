def f(a):
    return " ".join(map(str,a[::-1]))
n=int(input())
a=list(map(int,input().split()))
print(f(a))
