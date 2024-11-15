def f(s):
    if s.startswith('+'):
        a=s.split()
        if a[0][1:].isdigit() and len(a[0][1:]) in [2]:
            b=a[1]
            if len(b)==10 and b.isdigit() and sum(int(i) for i in b)>0:
                return ("Correct")
    return ("Incorrect")
s=input()
print(f(s))
