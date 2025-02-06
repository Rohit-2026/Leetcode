from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        t=[]
        for x in Counter(nums).most_common(k):
            t.append(x[0])
        return t    
                  
        