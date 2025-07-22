class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        i=0
        j=0
        d={}
        s=0
        m=0
        for j in nums:
            if j not in d:
                s+=j
                d[j]=1
                m=max(s,m)
            else:
                while d[j]>0:
                    s-=nums[i]
                    if d[nums[i]]>0:
                        d[nums[i]]-=1
                    else:
                        del d[nums[i]]
                    i+=1
                s+=j
                m=max(s,m)
                d[j]=1
        return m        

        