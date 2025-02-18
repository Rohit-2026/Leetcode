class Solution:
    def canJump(self, nums: List[int]) -> bool:
        c=0
        for i in range(len(nums)):
            if c<0:
                return False
            elif nums[i]>c:
                c=nums[i]
            c-=1
        return True         
        