class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        for i in range(n):
            for j in range(i+1,n):
                if i!=j:
                    matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in matrix:
            i=i.reverse()        
        return matrix            

        
        