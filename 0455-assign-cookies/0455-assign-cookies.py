class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i=0
        j=0
        c=0
        while i<len(g) and j<len(s):
            if g[i]<=s[j]:
                i+=1
                j+=1
                c+=1
            else:
                j+=1
        return c        


        