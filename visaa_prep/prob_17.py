def f(s):
    c=1
    a=""
    for i in range(1,len(s)):
        if s[i-1]==s[i]:
            c+=1
        else:
            a+=s[i-1]+str(c)
            c=1
    a+=s[-1]+str(c)
    return a
s=input()
print(f(s))
