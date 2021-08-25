class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.obsNum=0
        self.count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    self.start=[i,j]
                elif grid[i][j]==2:
                    self.end=[i,j]
                elif grid[i][j]==-1:
                    self.obsNum+=1
        self.visited=[]        
        
        def neighbors(grid,i,j):
            
            result=[]
            
            # top 
            if i-1 in range(len(grid)):
                if grid[i-1][j]!=-1:
                    result.append([i-1,j])
            # bottom 
            if i+1 in range(len(grid)):
                if grid[i+1][j]!=-1:
                    result.append([i+1,j])
            
            # left 
            if j-1 in range(len(grid[0])):
                if grid[i][j-1]!=-1:
                    result.append ([i,j-1])
                
            
            # right 
            if j+1 in range(len(grid[0])):
                if grid[i][j+1]!=-1:
                    result.append([i,j+1])
        
            return result        
        
        def dfs(grid,i,j):
            self.visited.append([i,j])
        
            for neighbor in neighbors(grid,i,j):
            
                if neighbor not in self.visited:
                
                    if neighbor==self.end:
                    
                        if len(self.visited)+self.obsNum+1==len(grid)*len(grid[0]):
                            self.count+=1 
                        
                        return 
                
                    self.visited.append(neighbor)
                
                    dfs(grid,neighbor[0],neighbor[1])
                    
                    
        dfs(grid,self.start[0],self.start[1])
                    
        return self.count
