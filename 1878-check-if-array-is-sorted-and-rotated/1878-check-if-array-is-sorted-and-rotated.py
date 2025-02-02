class Solution:
    def check(self, nums: List[int]) -> bool:
        c=0
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                if nums[i:]+nums[0:i]==sorted(nums):
                    c+=1
                    return True     
                else:
                    return False
        return True                  

        