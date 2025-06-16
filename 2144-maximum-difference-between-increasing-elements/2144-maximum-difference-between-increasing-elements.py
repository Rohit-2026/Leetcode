class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n=len(nums)
        m=nums[n-1]
        s=0
        for i in range(n-2,-1,-1):
            if nums[i]>m:
                m=nums[i]
            if m-nums[i]>s:
                s=m-nums[i]
        if s==0:
            return -1
        return s            

        