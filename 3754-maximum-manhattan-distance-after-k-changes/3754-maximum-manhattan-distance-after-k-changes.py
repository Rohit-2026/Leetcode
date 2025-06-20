class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        u, d, l, r = 0, 0, 0, 0
        max_dist = 0
        for i, c in enumerate(s):
            if c == 'N': 
                u += 1
            if c == 'S': 
                d += 1
            if c == 'W': 
                l += 1
            if c == 'E': 
                r += 1
            y,x=u-d,r-l
            dist=abs(x)+abs(y)
            max_dist=max(max_dist,dist+2*min(k,(i+1-dist)//2))  
        return min(max_dist,len(s))