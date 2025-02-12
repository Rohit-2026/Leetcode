from typing import List
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        d={}
        r=-1
        for n in nums:
            s=sum(int(d) for d in str(n))
            if s in d:
                r=max(r,d[s]+n)
                d[s]=max(d[s],n)
            else:
                d[s]=n
        return r
