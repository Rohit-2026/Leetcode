from itertools import permutations
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        c=set()
        n=len(tiles)
        for l in range(1,n+1):
            for i in permutations(tiles,l):
                c.add(i)
        return len(c)