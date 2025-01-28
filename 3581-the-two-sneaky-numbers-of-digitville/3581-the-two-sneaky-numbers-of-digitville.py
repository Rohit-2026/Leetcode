class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        t=set()
        j=[]
        for i in nums:
            if i not in t:
                t.add(i)
            else:
                j.append(i)
        return j            
        