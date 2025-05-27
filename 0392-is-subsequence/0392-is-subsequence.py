class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        j=0
        k=False
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                if i==len(s)-1:
                    k=True
                i+=1
                j+=1
            else:
                j+=1    
        return k
        