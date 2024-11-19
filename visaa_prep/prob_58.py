def f(s1,s2):
    d1={}
    d2={}
    for c1,c2 in zip(s1,s2):
        if c1 in d1:
            if d1[c1]!=c2:
                return "false"
        else:
            d1[c1]=c2
        if c2 in d2:
            if d2[c2]!=c1:
                return "false"
        else:
            d2[c2]=c1
    return "true"
n=int(input())
s1=input()
s2=input()
print(f(s1,s2))      
