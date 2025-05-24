class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        n=len(words)
        t=[]
        for i in range(n):
            if x in words[i]:
                t.append(i)
        return t        
        