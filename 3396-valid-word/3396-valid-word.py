class Solution:
    def isValid(self, word: str) -> bool:
        t=["A","E","I","O","U","a","e","i","o","u"]
        v=False
        c=False
        n=False
        for i in word:
            if i.isalpha():
                if i in t:
                    v=True
                else:
                    c=True 
            elif i.isdigit():
                n=True
            else:
                return False                   
        if v and c and len(word)>=3:
            return True
        else:
            return False                    


        