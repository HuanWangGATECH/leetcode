##1136. Parallel Courses

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
            
        
