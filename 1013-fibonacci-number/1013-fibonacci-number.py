class Solution:
    def fib(self, n: int) -> int:
        t=[0,1]
        for i in range(2,n+1):
            t.append(t[-1]+t[-2])
        return t[n]    
        