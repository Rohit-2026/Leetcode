class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors.extend(colors[:(k-1)])  
        c=0
        l=0
        for r in range(len(colors)):
            if r>0 and colors[r]==colors[r-1]:
                l=r
            if r-l+1>=k:
                c+=1  
        return c