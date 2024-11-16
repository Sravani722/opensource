def f(a):
    l=[]
    s=set()
    for i in a:
        if i not in s:
            s.add(i)
            l.append(i)
    return ' '.join(map(str,l))
n=int(input())
a=list(map(int,input().split()))
print(f(a))
