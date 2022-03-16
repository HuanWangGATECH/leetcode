# Can jump series on leetcode 


# similar questions 

https://leetcode.com/discuss/interview-question/1191163/Google-Phone-Screen/927967

 https://leetcode.com/problems/video-stitching/
 

https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/

google phone interview streetlights


## 1. can jump 1 
https://leetcode.com/problems/jump-game/submissions/

BFS 

```python 
from collections import deque 
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        
        #BFS with visited label 
        if not nums or len(nums)==0:
            return False 
        
        if len(nums)==1:
            return True 
        
        queue=deque()
        
        visited=[False]*len(nums)       
        queue.append(0)
        visited[0]=True 

        while queue:
            current_index=queue.popleft()
            
            new_range=min(current_index+nums[current_index],len(nums)-1)
            for new_index in range(1+current_index,new_range+1): 
                
                if new_index>=len(nums)-1:
                    return True 
                if not visited[new_index]:
                    queue.append(new_index)
                    visited[new_index]=True 
                
                
        return False 
```
# DFS solution (backtracking) solution 

```python 
from collections import deque 
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        
        def dfs(current_index):
            
            if current_index>=len(nums)-1:
                return True 
            
            furthest=min(current_index+nums[current_index],len(nums)-1)
            for new_index in range(current_index+1,furthest+1):
                
                if dfs(new_index):
                    return True 
                
            return False 
                
        
        return dfs(0)
  ```
  
  
  # Dp solution 
  ```python
  
  from collections import deque 
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        #DP
        n=len(nums)
        
        #dp[i] means if i can reach n-1 index 
        dp=n*[False]
        
        dp[n-1]=True 
        
        
        for i in range(n-2,-1,-1):
            
            minjump_index=min(n-1,nums[i]+i)
            
            for j in range(minjump_index,0,-1):
                
                if dp[j]:
                    dp[i]=True 
  
            
        return dp[0]
      ```
      
 # Greedy approach 
 
 
 ```java
 public class Solution {
    public boolean canJump(int[] nums) {
        int lastPos = nums.length - 1;
        for (int i = nums.length - 1; i >= 0; i--) {
            if (i + nums[i] >= lastPos) {
                lastPos = i;
            }
        }
        return lastPos == 0;
    }
}
```
## 2. can jump 2 


https://leetcode.com/problems/jump-game-ii/

# This is a nonweighed graph's shortest path problem BFS will solve this problem 

# my BFS solution 

```python
from collections import deque 
class Solution:
    def jump(self, nums: List[int]) -> int:
        
        queue=deque()
        
        queue.append(0)
        n=len(nums)
        distance=[math.inf]*n
        distance[0]=0
        while queue:
            
            current_index=queue.popleft()
            minjump=min(current_index+nums[current_index],n-1)
            for next_index in range(current_index+1,minjump+1):
                if distance[next_index]>distance[current_index]+1:
                    distance[next_index]=distance[current_index]+1
                    queue.append(next_index)
                    
        
        return distance[n-1]
```



# Dp solution 

```python

class Solution:
    def jump(self, nums: List[int]) -> int:
        
    # Dp solution 
    

    
        #dp[i] minimum number of jumps to reach n-1
    
        n=len(nums)
        dp=[math.inf]*n
    
        dp[n-1]=0
    
        for i in range(n-2,-1,-1):
            minJump=min(nums[i]+i,n-1)
            for j in range(minJump,i,-1):
                dp[i]=min(dp[i],dp[j]+1)
                #print (i,j,dp)
        #print (dp)
        return dp[0]
 ```
 
 
 
# 3 video stiching 

https://leetcode.com/problems/video-stitching/


# BFS graph sssp 

```python
from collections import deque 
class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips=sorted(clips)
        
        #graph BFS sssp 
        #build graph 
        #print (clips)
        graph={}
        
        for i in range(len(clips)):
            graph[i]=[]
            
      
        for i in range(len(clips)):
            
            for j in range(i+1,len(clips)):
                i_begin=clips[i][0]
                i_end=clips[i][1]
                
                j_begin=clips[j][0]
                j_end=clips[j][1]
                if j_begin<=i_end and j_end>i_end:
                    graph[i].append(j)

        queue=deque()
        if clips[0][0]>0:
            return -1
        if clips[-1][1]<time:
            return -1
        queue.append(0)
        
        dist=len(clips)*[math.inf]
        dist[0]=1
        while queue:
            
            curr_index=queue.popleft()
            for nei in graph[curr_index]:
                if dist[nei]>dist[curr_index]+1:
                    dist[nei]=dist[curr_index]+1
                    queue.append(nei)
        
        print (dist)
        return dist[len(clips)-1]
```


