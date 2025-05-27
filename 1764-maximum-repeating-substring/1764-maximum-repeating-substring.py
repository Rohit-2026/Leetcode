class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        if len(word)>=len(sequence):
            if word in sequence:
                return 1
            else:
                return 0
        a=1
        s=word
        k=0
        while len(word)<=len(sequence): 
            if a>=k and word in sequence:
                k=a
            word+=s
            a+=1       
        return k               
        