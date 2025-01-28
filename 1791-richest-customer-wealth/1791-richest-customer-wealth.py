class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        t=0
        for i in accounts:
            t=max(t,sum(i))
        return t    
        