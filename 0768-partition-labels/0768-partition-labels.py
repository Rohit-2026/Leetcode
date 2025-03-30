class Solution(object):
    def partitionLabels(self,s):
        last={c:i for i, c in enumerate(s)}
        res,f,l=[],0,0
        for i, c in enumerate(s):
            f=max(f,last[c])
            if i==f:
                res.append(f-l+1)
                l=i+1
        return res
