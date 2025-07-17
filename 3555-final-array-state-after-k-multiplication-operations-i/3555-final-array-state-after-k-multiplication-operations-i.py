import heapq
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        t=[]
        heap=[]
        for i in range(len(nums)):
            t.append((nums[i],i))
        for i in t:
            heapq.heappush(heap,i)
        while k:
            i=heapq.heappop(heap)
            heapq.heappush(heap,(i[0]*multiplier,i[1]))   
            k-=1 
        t=[0]*len(nums)
        while heap:
            v,i=heapq.heappop(heap)
            t[i]=v    
        return t
        