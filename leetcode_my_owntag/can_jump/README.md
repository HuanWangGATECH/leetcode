# Can jump series on leetcode 

## 1. can jump 1 

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

## 2. can jump 2 
