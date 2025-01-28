class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        b=nums[0:n]
        b1=nums[n:]
        t=[]
        for i in range(n):
            t.append(b[i])
            t.append(b1[i])
        return t    

        