class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        t=[0]*(len(nums))
        for i in nums:
            t[i-1]=1
        n=len(t)    
        for i in range(n):
            if t[i]==0:
                t.append(i+1)
        for i in range(n):
            t.pop(0)            
        return t
                    
                    
        
        