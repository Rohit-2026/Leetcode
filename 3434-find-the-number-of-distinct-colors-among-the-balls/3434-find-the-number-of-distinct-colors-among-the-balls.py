class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        n=len(queries)
        s=[0]*n
        mp={}
        co=defaultdict(int)
        i=0
        for x, c in queries:
            if x in mp:
                c0=mp[x]
                co[c0]-=1
                if co[c0]==0:
                    co.pop(c0)
            mp[x]=c
            co[c]+=1
            s[i]=len(co)
            i+=1
        return s
        