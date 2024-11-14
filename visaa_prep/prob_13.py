def f(n):
    if (n%400==0) or (n%100!=0 and n%4==0):
        print("YES")
    else:
        print("NO")
n=int(input())
f(n)
