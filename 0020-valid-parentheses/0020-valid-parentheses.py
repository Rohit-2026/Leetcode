class Solution:
    def isValid(self, s: str) -> bool:
        t=[s[0]]
        for i in range(1,len(s)):
            if len(t)>0:
                if t[-1]=="(" and s[i]==")":
                    t.pop()
                elif t[-1]=="{" and s[i]=="}":
                    t.pop()
                elif t[-1]=="[" and s[i]=="]":
                    t.pop() 
                else:
                    t.append(s[i])       
            else:
                t.append(s[i])
        if len(t)>0:
            return False    
        else:
            return True          
        