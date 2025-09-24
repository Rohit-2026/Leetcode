class Solution:
    def longestPalindrome(self, s: str) -> int:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        c=0
        m=0
        t=0
        for i in d: 
            if d[i]%2==0:
                c+=d[i]
            else:
                c+=d[i]-1
                t=1
        if t:
            return(c+1)
        else:
            return c                

        