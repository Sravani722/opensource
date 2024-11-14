def f(x):
    if (x-100)<(x-(0.10*x)):
        return x-100
    else:
        return x-(0.10*x)
x=int(input())
print(int(f(x)))
