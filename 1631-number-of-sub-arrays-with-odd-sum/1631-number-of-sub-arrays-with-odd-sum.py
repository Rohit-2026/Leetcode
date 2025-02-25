class Solution:
    def numOfSubarrays(self, arr):
        MOD=1000000007
        p_c={0: 1}
        p_s=0
        r=0
        for i in arr:
            p_s+=i
            if p_s%2==1:
                r=(r+p_c.get(0,0))%MOD
            else:
                r=(r+p_c.get(1,0))%MOD
            p_c[p_s%2]=p_c.get(p_s%2,0)+1
        return r