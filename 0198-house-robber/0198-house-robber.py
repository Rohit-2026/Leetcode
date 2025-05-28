class Solution:
    def rob(self, nums: List[int]) -> int:
        t=[nums[0]]
        if len(nums)>=2:
            t.append(max(nums[1],nums[0]))
        else:
            return t[0]    
        for i in range(2,len(nums)):
            t.append(max(nums[i]+t[i-2],t[i-1]))
        return max(t)