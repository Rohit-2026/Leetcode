class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        c={}
        for i in d:
            if d[i] in c:
                c[d[i]]+=1
                return False
            else:
                c[d[i]]=1
        return True        


        