class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        d={}
        t=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]*nums[j] not in d:
                    d[nums[i]*nums[j]]=1
                else:
                    d[nums[i]*nums[j]]+=1    
        for i in d:
            if d[i]>1:
                t+=(d[i]**2-d[i])*4
        return t
