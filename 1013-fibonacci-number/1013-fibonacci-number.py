class Solution:
    def fib(self, n: int) -> int:
        a=[0]*(n+1)
        def fibb(n):
            if n in [0,1]:
                return n
            if a[n]!=0:
                return a[n]
            a[n]=fibb(n-1)+fibb(n-2) 
            return a[n]
        return fibb(n)    


        