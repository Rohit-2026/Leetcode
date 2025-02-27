class Solution:
    def lenLongestFibSubseq(self, nums: List[int]) -> int:
        mpp={nums[i]: i for i in range(len(nums))}
        d={}
        r=0
        for j in range(1,len(nums)):
            for i in range(j):
                if nums[j]-nums[i] in mpp and mpp[nums[j]-nums[i]]<i:
                    d[i,j]=d.get((mpp[nums[j]-nums[i]], i),0)+1
                    r=max(r,d[i, j])
        return r+2 if r>0 else 0