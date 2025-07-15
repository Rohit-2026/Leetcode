class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n=1000
        m=""
        for i in strs:
            if n>len(i):
                n=min(n,len(i))
                m=i
        t=""     
        f=True 
        for i in range(n):
            for j in strs:
                if j[i]!=m[i]:
                    f=False
            if f==False:
                break
            else:
                t+=m[i]         

        return t
        