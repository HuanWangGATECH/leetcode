#BFS solution 

from collections import deque 
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
      
        
        res=[]
        
        n=len(graph)
        indegree=[0]*n
        reverse={}
        
        for i in range(n):
            reverse[i]=[]
            
        for i in range(n):
            
            neis=graph[i]
            
            for nei in neis:
                indegree[i]+=1 
                reverse[nei].append(i)
                
        
                
        
        queue=deque()
        
        for i in range(n):
            if indegree[i]==0:
                queue.append(i)
                
        result=[]        
        while queue:
            u=queue.popleft() 
            result.append(u)
            for v in reverse[u]:
                indegree[v]-=1 
                if indegree[v]==0:
                    queue.append(v)
            
        return sorted(result)
                
   ## DFS solution 


from collections import deque 
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
      
        
        
        
        n=len(graph)
        visited=[0]*n
        res=[]
        
        for i in range(n):
            if not self.dfs(i,graph,visited):
                res.append(i)
         
        return res 
    
    def dfs(self,u,graph,visited):
        # return True if cycle detected 
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
                
        
        
