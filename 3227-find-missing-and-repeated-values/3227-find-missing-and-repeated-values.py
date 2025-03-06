class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        t=set()
        f=0
        k=[]
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] not in t:
                    t.add(grid[i][j])
                else:
                    k.append(grid[i][j])
        for i in range(1,len(grid)*len(grid)+1):
            if i not in t:
                k.append(i)
                break
        return k                