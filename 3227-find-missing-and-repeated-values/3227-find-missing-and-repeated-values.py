class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        t=set()
        f=0
        k=[]
        l=len(grid)
        for i in range(l):
            for j in range(l):
                if grid[i][j] not in t:
                    t.add(grid[i][j])
                else:
                    k.append(grid[i][j])
        for i in range(1,l*l+1):
            if i not in t:
                k.append(i)
                break
        return k                