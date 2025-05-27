class Solution:
    def climbStairs(self, n: int) -> int:
        m=[1,2]
        for i in range(2,n):
            m.append(m[-1]+m[-2])
        return m[n-1]    

        