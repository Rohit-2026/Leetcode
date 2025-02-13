import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        c=0
        while nums[0]<k:
            if len(nums)<2:
                break
            x=heapq.heappop(nums)
            y=heapq.heappop(nums)
            heapq.heappush(nums,min(x,y)*2+max(x,y))
            c+=1
        return c