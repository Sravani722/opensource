def f(a):
    a.sort(reverse=True)
    for i in range(len(a)-2):
        if a[i]<a[i+1]+a[i+2]:
            return a[i]+a[i+1]+a[i+2]
    return -1
n=int(input())
a=list(map(int,input().split()))
print(f(a))
