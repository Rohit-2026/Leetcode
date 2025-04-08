class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(set(nums))==len(nums):
            return 0
        else:
            c=0
            while len(set(nums))!=len(nums):
                if len(nums)<=3:
                    c+=1
                    break
                nums=nums[3:]
                c+=1 
            return c    

        