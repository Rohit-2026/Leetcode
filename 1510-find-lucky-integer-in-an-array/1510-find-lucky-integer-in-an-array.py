from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d=Counter(arr)
        m=-1
        for i in d:
            if d[i]==i:
                m=max(m,i)
        return m        

        