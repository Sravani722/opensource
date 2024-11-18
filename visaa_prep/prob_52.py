def f(s):
    v=0
    c=0
    for i in s:
        if i.lower() in 'aeiou':
            v+=1
        elif i.isalpha():
            c+=1
    r=(v,c)
    return ",".join(map(str,r))
s=input()
print(f(s))
