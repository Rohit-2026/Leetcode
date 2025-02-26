from itertools import accumulate
from typing import List
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        p_s=list(accumulate(nums))
        mx_s=max(0,max(p_s))
        mi_s=min(0,min(p_s))
        return mx_s-mi_s
