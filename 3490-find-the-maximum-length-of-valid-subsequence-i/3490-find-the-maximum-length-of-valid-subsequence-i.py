class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        m=0
        o=0
        e=0
        for i in nums:
            if i%2==0:
                e+=1
            else:
                o+=1
        m=max(o,e)
        t=[1]
        for i in range(1,len(nums)):
            if nums[i]%2!=nums[i-1]%2:
                t.append(t[-1]+1)
        return max(m,t[-1])        


            


        