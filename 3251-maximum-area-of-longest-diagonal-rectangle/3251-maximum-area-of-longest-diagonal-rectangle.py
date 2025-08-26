class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        ma=0
        md=0
        for i in dimensions:
            if i[0]*i[0]+i[1]*i[1]>md:
                md=i[0]*i[0]+i[1]*i[1]
                ma=i[0]*i[1]
            elif i[0]*i[0]+i[1]*i[1]==md and i[0]*i[1]>ma:
                ma=i[0]*i[1]
        return ma        
        