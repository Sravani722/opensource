from collections import Counter
def missingNumbers(arr, brr):
    a=Counter(arr)
    b=Counter(brr)
    r=[]
    for i in b:
        if b[i]>a.get(i,0):
            r.append(i)
    r.sort()
    return r
