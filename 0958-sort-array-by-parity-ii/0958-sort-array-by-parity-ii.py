class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        t=[0]*len(nums)
        o=1
        e=0
        for i in nums:
            if i%2==0:
                t[e]=i
                e+=2
            else:
                t[o]=i
                o+=2
        return t


        