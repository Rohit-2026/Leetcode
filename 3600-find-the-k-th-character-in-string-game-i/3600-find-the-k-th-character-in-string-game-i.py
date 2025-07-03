class Solution:
    def kthCharacter(self, k: int) -> str:
        n=1
        w="a"
        while len(w)<k:
            t=""
            for i in w:
                t+=chr(ord(i)+1%96)
            w+=t  
        return w[k-1]      
        