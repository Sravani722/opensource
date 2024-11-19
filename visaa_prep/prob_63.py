class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cs={}
        ct={}
        for i in s:
            cs[i]=cs.get(i,0)+1
        for j in t:
            ct[j]=ct.get(j,0)+1
        return cs==ct
        
