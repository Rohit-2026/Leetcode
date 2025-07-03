class Solution:
    def kthCharacter(self, k: int) -> str:
        n=1
        w="a"
        while n<k:
            t=""
            for i in w:
                t+=chr(ord(i)+1%96)
            w+=t  
            n*=2
        return w[k-1]      
        