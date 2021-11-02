##1136. Parallel Courses
## my BFS solution 
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        
        sortedOrder=[]
        
        # build a graph 
        graph={}
        indegree=[0]*(n+1)
        for i in range(1,n+1):
            graph[i]=[]
           
        
        
        for relation in relations:
            prevCourse=relation[0]
            nextCourse=relation[1]
            indegree[nextCourse]+=1 
            graph[prevCourse].append(nextCourse)
        
        
        #print (graph )
        sources=[]
        for u,i in enumerate(indegree):
            if i==0 and u >0:
                sources.append(u)
                
        #print (sources)
        new_source=[]
        step=0
        while sources:
            u=sources.pop(0)

            sortedOrder.append(u)
            
            for v in graph[u]:
                
                indegree[v]-=1 
                if indegree[v]==0:
                    new_source.append(v)
            if sources==[]:
                sources=new_source
                new_source=[]
                step+=1 
                
        if len(sortedOrder)==n:
            return step 
        else:
            return -1
            
     ### DFS solution still need some time  
    
    
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        
       
        
        # build a graph 
        graph={}
        visited={}
        depth={}
        
        for i in range(1,n+1):
            graph[i]=[]
            visited[i]=False
          
            
        for relation in relations:
            prevCourse=relation[0]
            nextCourse=relation[1]
            graph[prevCourse].append(nextCourse) 
            
          
        
        for i in range(1,n+1):
            #print (i,self.dfs(i,graph,visited))
            if self.dfs(i,graph,visited):
                return -1
         
        return False 
        #print (sortedOrder)
                
    def dfs(self,u,graph,visited):
       ## there are two kinds of visited nodes 
     #1, visited but its's still being processed in the dfs process, therefore upstream to the current 
     #2, visited and all lower level dfs processed 
     # if exploring encounter #1 nodes, there is a cycle 
     # if exploring encounter # 2 nodes, no cycle 
        
        print (visited,graph)
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
