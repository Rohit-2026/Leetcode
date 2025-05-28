class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        t=obstacleGrid
        if t[0][0]==0:
            t[0][0]=1
        else:
            t[0][0]=0    
        for i in range(1,len(t[0])):
            if t[0][i]==0:
                t[0][i]=t[0][i-1]
            else:
                t[0][i]=0    
        for j in range(1,len(t)):
            if t[j][0]==0:
                t[j][0]=t[j-1][0]
            else:
                t[j][0]=0    
        for i in range(1,len(t)):
            for j in range(1,len(t[0])):
                if t[i][j]==0:
                    t[i][j]=t[i][j-1]+t[i-1][j]   
                else:
                    t[i][j]=0            
        return t[-1][-1]    
         


        