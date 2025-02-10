class Solution:
    def clearDigits(self, s: str) -> str:
        t=[]
        for i in range(len(s)):
            if s[i].isdigit():
                if t:
                    t.pop()
                else:
                    t.append(s[i])    
            else:
                t.append(s[i])
        return "".join(t)                



        