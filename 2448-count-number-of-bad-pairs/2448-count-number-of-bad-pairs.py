from collections import defaultdict
class Solution:
    def countBadPairs(self, nums):
        n=len(nums)
        c=n*(n-1)//2
        d=defaultdict(int)
        for i,num in enumerate(nums):
            diff =num - i
            c-= d[diff]
            d[diff] += 1
        return c