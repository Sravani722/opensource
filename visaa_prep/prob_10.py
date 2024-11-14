def f(v,c):
    if (v=='R' and c=='P') or (v=='P' and c=='S') or (v=='S' and c=='R'):
        print("Charan")
    elif (v=='P' and c=='R') or (v=='S' and c=='P') or (v=='R' and c=='S'):
        print("Vignesh")
    else:
        print("NULL")
v,c=map(str,input().split())
f(v,c)
