class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        #print (obstacleGrid)
        
    
        
        rows,cols=len(obstacleGrid),len(obstacleGrid[0])
        
        
       
        

        if rows==1 and cols==1:
            if obstacleGrid[0][0]==1:
                return 0
            else:
                return 1
        
        arr=[[0 for i in range(cols)] for j in range(rows)]
        
        #print (arr)
        #print (obstacleGrid)
        
        for i in range(cols):
            if obstacleGrid[0][i]!=1:
                arr[0][i]=1
            else:
                break 
        for j in range(rows):
            print (j)
            if obstacleGrid[j][0]!=1:
                arr[j][0]=1
            else:
                break   
        
        arr[0][0]=0
               
        
        for i in range(1,cols):
            for j in range(1,rows):
                
                if obstacleGrid[j][i]==1:
                    arr[j][i]=0
                else:
                    top=arr[j-1][i]
                    left=arr[j][i-1]
                    arr[j][i]=top+left

        return arr[-1][-1]
        

        
