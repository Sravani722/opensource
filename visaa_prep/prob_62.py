class Solution:
    def romanToInt(self, s: str) -> int:
        v={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        pv=0
        t=0
        for i in reversed(s):
            cv=v[i]
            if cv<pv:
                t-=cv
            else:
                t+=cv
            pv=cv
        return t
