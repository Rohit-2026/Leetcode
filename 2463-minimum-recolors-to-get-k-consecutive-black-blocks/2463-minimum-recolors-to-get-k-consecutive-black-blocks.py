class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        cb=0
        cw=0
        t=10000
        for i in range(k):
            if blocks[i]=="W":
                cw+=1
            else:
                cb+=1
        t=min(t,cw)        
        i=0
        j=k     
        while j<len(blocks):
            if blocks[i]=="B":
                cb-=1
            else:
                cw-=1
            i+=1    
            if blocks[j]=="W":
                cw+=1
            else:
                cb+=1
            j+=1
            t=min(t,cw)
        return max(t,0)