class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<0:
            return False
        elif bin(n).count('1')==1:
            return True
        else:
            return False    
        