class Solution:
    def isPalindrome(self, s: str) -> bool:
        t=""
        for i in s:
            if i.isalpha():
                t+=i.lower()
            elif i.isdigit():
                t+=i    
        i=0
        j=len(t)-1
        while i<j:
            if t[i]==t[j]:
                i+=1
                j-=1
            else:
                return False
        return True                    
        