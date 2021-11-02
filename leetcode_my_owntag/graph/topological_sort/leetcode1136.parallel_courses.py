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
    
    
    def minimumSemesters(self, N, relations):
    """
    :type N: int
    :type relations: List[List[int]]
    :rtype: int
    """
    n = N        
    d = collections.defaultdict(list)
    visited = [0 for _ in range(n + 1)]
    depth = [1 for _ in range(n + 1)]
    for x, y in relations:
        d[y].append(x)
    for i in range(1, n + 1):
        if not self.dfs(i, d, visited, depth, 1):
            return -1
    return max(depth)

def dfs(self, i, d, visited, depth, cnt):
    if visited[i] == 1:
        return False
    if visited[i] == 2:
        return True
    visited[i] = 1
    for j in d[i]:
        depth[i] = max(depth[i], depth[j] + 1)
        if not self.dfs(j, d, visited, depth, cnt):
            return False
    visited[i] = 2
    return True



