class Solution:
    def reverseVowels(self, s: str) -> str:
        v=set('aeiouAEIOU')
        sl=list(s)
        l=0
        r=len(s)-1
        while l<r:
            while l<r and sl[l] not in v:
                l+=1
            while l<r and sl[r] not in v:
                r-=1
            sl[l],sl[r]=sl[r],sl[l]
            l+=1    
            r-=1
        return "".join(sl)
