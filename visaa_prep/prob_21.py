def f(x):
    if x>=30:
        return "YES"
    else:
        return "NO"
t=int(input())
for _ in range(t):
    x=int(input())
    print(f(x))
