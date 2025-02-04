class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        m=0
        c=nums[0]
        if len(nums)==1:
            return nums[0]
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                c+=nums[i]
                m=max(m,c)
            else:
                m=max(m,c)
                c=nums[i] 
        return m        
        