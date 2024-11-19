class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ms=set()
        l=0
        ml=0
        for r in range(len(s)):
            while s[r] in ms:
                ms.remove(s[l])
                l+=1
            ms.add(s[r])
            
            ml=max(ml,r-l+1)
        return ml
        
        
