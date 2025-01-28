class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        t=[]
        for i in accounts:
            t.append(sum(i))
        return max(t)    
        