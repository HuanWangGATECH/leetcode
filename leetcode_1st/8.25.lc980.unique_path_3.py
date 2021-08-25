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

    
    
    class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        numObstacles = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 2:
                    end = (i, j)
                elif grid[i][j] == -1:
                    numObstacles += 1
        
        def findNeighbors(node):
            x, y = node
            temp = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
            actual = []
            for each in temp:
                ex, ey = each
                if ex < 0 or ey < 0 or ex > m - 1 or ey > n - 1 or grid[ex][ey] == -1:
                    continue
                else:
                    actual.append(each)
                    
            return actual
        
        visited = set()
        self.cnt = 0
        
        def func(node):
            if node == end:
                #print(len(visited))
                if len(visited) == m * n - numObstacles:
                    self.cnt += 1
                return
            
            for neighbor in findNeighbors(node):
                if neighbor not in visited:
                    visited.add(neighbor)
                    func(neighbor)
                    visited.remove(neighbor)
        
        visited.add(start)
        func(start)
        #print(numObstacles)
        return self.cnt
