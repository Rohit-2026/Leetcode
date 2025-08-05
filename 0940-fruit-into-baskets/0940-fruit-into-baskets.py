class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d={}
        i=0
        j=0
        c=0
        while j<len(fruits):
            if len(d)>1 and fruits[j] not in d:
                if d[fruits[i]]==1:
                    del d[fruits[i]]
                else:
                    d[fruits[i]]-=1
                i+=1
            else:
                if fruits[j] not in d:
                    d[fruits[j]]=1
                else:
                    d[fruits[j]]+=1
                c=max(c,j-i+1)    
                j+=1    
        return c              

        