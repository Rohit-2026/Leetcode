class Solution:
    def countBits(self, n: int) -> List[int]:
        t=[0]
        for i in range(1,n+1):
            if (i)&(i-1)==0:
                t.append(1)
                k=i
            else:
                t.append(1+t[i-k])
        return t          
        