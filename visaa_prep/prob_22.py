def f(n):
    if (sum(int(i) for i in str(n)))%2==0:
        return "Vignesh"
    else:
        return "Charan"
n=int(input())
print(f(n))
