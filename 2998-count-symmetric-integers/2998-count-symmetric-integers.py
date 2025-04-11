class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        c=0
        l=low
        h=high
        for num in range(l,h+1):
            s=str(num) 
            n=len(s)
            if n%2!=0:
                continue
            m=n//2
            l=sum(int(s[i]) for i in range(m))
            r=sum(int(s[i]) for i in range(m,n))  
            if l==r:
                c+=1
        return c