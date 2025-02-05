class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1==s2:
            return True
        d=[]
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                d.append(i)
            if len(d)>2:
                return False
        if len(d)!=2:
            return False
        s1_list=list(s1)
        i,j=d[0],d[1]
        s1_list[i],s1_list[j]=s1_list[j],s1_list[i]
        return "".join(s1_list)==s2
