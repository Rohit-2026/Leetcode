class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d={}
        j=len(s1)
        d1={}
        if len(s1)>len(s2):
            return False
        for i in range(j):
            if s1[i] not in d1:
                d1[s1[i]]=1
            else:
                d1[s1[i]]+=1
        for i in range(j):
            if s2[i] not in d:
                d[s2[i]]=1
            else:
                d[s2[i]]+=1
        i=0
        j=len(s1)-1        
        while j<len(s2)-1:
            if d1==d:
                return True
            if d[s2[i]]>1:
                d[s2[i]]-=1
            else:
                del d[s2[i]]
            i+=1    
            j+=1
            if s2[j] not in d:
                d[s2[j]]=1
            else:
                d[s2[j]]+=1
        return d==d1         



        