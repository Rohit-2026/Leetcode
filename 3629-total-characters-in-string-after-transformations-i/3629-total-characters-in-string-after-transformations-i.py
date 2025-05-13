class Solution:
    def lengthAfterTransformations(self,s:str,t:int)->int:
        m=10**9+7
        c=[0]*26
        for ch in s:
            c[ord(ch)-97]+=1
        for i in range(t):
            n=[0]*26
            n[0]=c[25]
            n[1]=(c[25]+c[0])%m
            for i in range(2,26):
                n[i]=c[i-1]
            c=n
        return sum(c)%m
