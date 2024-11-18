def f(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end="")
        s=2*(n-i)
        print(" "*s,end="")
        for j in range(i,0,-1):
            print(j,end="")
        print()
n=int(input())
f(n)
