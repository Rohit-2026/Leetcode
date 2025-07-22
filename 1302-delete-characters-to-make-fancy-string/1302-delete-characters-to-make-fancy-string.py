class Solution:
    def makeFancyString(self, s: str) -> str:
        t=""
        for i in s:
            if len(t)>=2:
                if t[-1]==t[-2]==i:
                    continue
                else:
                    t+=i
            else:
                t+=i
        return t                    

        