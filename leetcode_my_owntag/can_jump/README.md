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
