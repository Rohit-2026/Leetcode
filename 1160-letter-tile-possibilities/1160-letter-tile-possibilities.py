from math import factorial
from collections import Counter
class Solution:
    def numTilePossibilities(self,tiles:str)->int:
        freq=Counter(tiles)
        unique_tiles=list(freq.keys())
        total=0
        counts=[0]*len(unique_tiles)
        while True:
            if sum(counts)>0:
                k=sum(counts)
                ways=factorial(k)
                for count in counts:
                    ways//=factorial(count)
                total+=ways
            i=len(unique_tiles)-1
            while i>=0:
                if counts[i]<freq[unique_tiles[i]]:
                    counts[i]+=1
                    for j in range(i+1,len(unique_tiles)):
                        counts[j]=0
                    break
                i-=1
            if i<0:
                break
        return total
