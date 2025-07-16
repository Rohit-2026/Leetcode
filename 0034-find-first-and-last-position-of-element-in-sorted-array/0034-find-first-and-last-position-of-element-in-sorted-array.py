import bisect
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=bisect.bisect_left(nums,target)
        h=bisect.bisect_right(nums,target)
        if l<h:
            return [l,h-1]
        else:
            return [-1,-1]    
        

        