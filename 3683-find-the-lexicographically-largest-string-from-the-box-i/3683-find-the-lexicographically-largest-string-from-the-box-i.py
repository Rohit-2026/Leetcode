class Solution(object):
    def answerString(self, word, numFriends):
        if numFriends==1:
            return word
        r=""
        l=len(word)-numFriends+1
        for i in range(0,len(word)):
            t=word[i:i+l]
            if t>r:
                r=t
        return r