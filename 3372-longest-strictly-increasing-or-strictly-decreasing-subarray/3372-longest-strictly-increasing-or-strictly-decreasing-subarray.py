class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        m=a=d=1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                a+=1
                d=1
            elif nums[i]<nums[i-1]:
                d+=1
                a=1
            else:
                a= d=1
            m=max(m,a,d)
        return m