def f(n):
    if 3<=n and n<=5:
        print("Spring")
    elif 6<=n and n<=8:
        print("Summer")
    elif 9<=n and n<=11:
        print("Autumn")
    elif n==12 or n==1 or n==2:
        print("Winter")
    else:
        print("Invalid")
n=int(input())
f(n)
