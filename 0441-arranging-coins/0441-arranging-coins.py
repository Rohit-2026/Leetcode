class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((math.isqrt(1+8*n)-1)//2)


        