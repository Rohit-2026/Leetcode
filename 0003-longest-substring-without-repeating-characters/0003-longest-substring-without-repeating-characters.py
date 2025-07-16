class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d={}
        i=0
        j=0
        c=0
        while i<len(s) and j<len(s):
            if s[j] not in d:
                d[s[j]]=1
                j+=1
            else:
                while d.get(s[j],0)>0:
                    d[s[i]]-=1
                    if d[s[i]]==0:
                        del d[s[i]]
                    i+=1   
            c=max(c,j-i)         
        return c                    


        