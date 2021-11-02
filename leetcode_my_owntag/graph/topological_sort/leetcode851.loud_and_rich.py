![GitHub Logo](/images/logo.png)

from collections import deque
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n=len(quiet)
        ans=[-1]*n
        
        graph={}
        
        for i in range(n):
            graph[i]=[]
        
        
        for u,v in richer:
            graph[v].append(u)
            
            
        for u in range(n):
            if ans[u]==-1:
                self.dfs(u,graph,ans,quiet)
    
        return ans
    
    def dfs(self,u,graph,ans,quiet):
        
        ans[u]=u
        for v in graph[u]:
            self.dfs(v,graph,ans,quiet)
            if quiet[ans[v]] < quiet[ans[u]]:
                ans[u]=ans[v]
        
        
