class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        
        graph={}
        visited=[0]*numCourses
        for i in range(numCourses):
            graph[i]=[]
            
            
        for pre in prerequisites:
            u=pre[0]
            v=pre[1]
            graph[u].append(v)
        
        for i in range(numCourses):
            
            if self.dfs(i,graph,visited):
                return False 
        
        return True 
            
        
    def dfs(self,u,graph,visited):
        #returns True if cycle detected 
        
        if visited[u]==1:
            return True
        if visited[u]==2:
            return False 
        visited[u]=1
        
        for v in graph[u]:
            
            if self.dfs(v,graph,visited):
                return True 
            
        visited[u]=2
        return False 
    
        
        
        
