def f(a):
    for i in range(1,len(a)):
        if a[i-1]>a[i]:
            return "false"
    return "true"
n=int(input())
a=list(map(int,input().split()))
print(f(a))
