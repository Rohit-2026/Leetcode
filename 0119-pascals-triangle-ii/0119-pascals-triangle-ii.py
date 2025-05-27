class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        t=[[1]]
        for i in range(1,rowIndex+1):
            k=[1]*(i+1)
            for j in range(1,i):
                k[j]=t[i-1][j-1]+t[i-1][j]
            t.append(k)
        return t[-1]
        