def f(a,k):
    l=0
    h=len(a)-1
    while l<=h:
        m=(l+h)//2
        if a[m]==k:
            return m
        elif a[m]<k:
            l=m+1
        else:
            h=m-1
    return -1
n=int(input())
a=list(map(int,input().split()))
k=int(input())
print(f(a,k))
