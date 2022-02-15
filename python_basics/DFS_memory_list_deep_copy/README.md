https://leetcode.com/problems/permutations/discuss/18284/Backtrack-Summary%3A-General-Solution-for-10-Questions!!!!!!!!-Python-(Combination-Sum-Subsets-Permutation-Palindrome)


```python
    def combinationSum(self, candidates, target):
        def backtrack(tmp, start, end, target):
            if target == 0:
                ans.append(tmp[:])
            elif target > 0:
                for i in range(start, end):
                    tmp.append(candidates[i])
                    backtrack(tmp, i, end, target - candidates[i])
                    tmp.pop()
        ans = [] 
        candidates.sort(reverse= True)
        backtrack([], 0, len(candidates), target)
        return ans
```

# Would you mind explaining why we should append nums[:] and not nums? If nums[:] returns a modified copy, shouldn't nums be pointing to the modified object and hence is valid for append as well? Thanks in advance.


https://stackoverflow.com/questions/32448414/what-does-colon-at-assignment-for-list-do-in-python



https://www.geeksforgeeks.org/python-cloning-copying-list/




```
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        paths=[]
        
        self.dfsTree(root,paths,"")
    
        return paths
    
    
    def dfsTree(self,node,paths,path):
        
        
     
        path+=str(node.val)
        
        print (paths,hex(id(paths)),path,hex(id(path)))
             
        if node.left:
            self.dfsTree(node.left,paths,path+'->')
        if node.right:
          
            self.dfsTree(node.right,paths,path+'->')
        
        
        if not node.left and not node.right:
            paths.append(path)  
            
        print (paths,hex(id(paths)),path,hex(id(path)))   
        
    ```
    
    Output is 
    
    ```python
[] 0x7fe2318ffec0 1 0x7fe23170c8b0
[] 0x7fe2318ffec0 1->2 0x7fe23170fa70
[] 0x7fe2318ffec0 1->2->5 0x7fe2317586b0
['1->2->5'] 0x7fe2318ffec0 1->2->5 0x7fe2317586b0
['1->2->5'] 0x7fe2318ffec0 1->2 0x7fe23170fa70
['1->2->5'] 0x7fe2318ffec0 1->3 0x7fe231758970
['1->2->5', '1->3'] 0x7fe2318ffec0 1->3 0x7fe231758970
['1->2->5', '1->3'] 0x7fe2318ffec0 1 0x7fe23170c8b0
    ```
    path here is a immutatble string variable that gets a new memory in each dfsTree call. Therefore, the outside dfsTree's path variable doesn't retain the inside dfsTree 
    
    ![dfsTree_memory]()
    
    
    
    
