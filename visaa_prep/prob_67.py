class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        b=[[]]
        for i in nums:
            s=[]
            for n in b:
                ss=n+[i]
                s.append(ss)
            b.extend(s)
        return b
