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
                
        
