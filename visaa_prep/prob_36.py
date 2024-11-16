from collections import Counter
def f(a):
    
    d=Counter(a)
    for i,v in d.items():
        if v==1:
            return i
n=int(input())
a=list(map(int,input().split()))
print(f(a))
