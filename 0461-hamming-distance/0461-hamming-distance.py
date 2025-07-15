class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        t1=bin(x)[2:][::-1]
        t2=bin(y)[2:][::-1]
        c=0
        for i in range(min(len(t1),len(t2))):
            if t1[i]!=t2[i]:
                c+=1
        if len(t1)>len(t2):
            c+=t1[len(t2):].count("1")
        else:
            c+=t2[len(t1):].count("1")
        return c

        
        
        