
'''
Problem Statement 

Given a binary tree, populate an array to represent its level-by-level traversal. 

You should populate the values of all nodes of each level from left to right in separate sub-arrays.

'''

https://leetcode.com/playground/4bEfuunb

```python 
def treeTraverseBFS(node):
    
    queue=[]
    queue.append(node)
    res=[]
    while queue:
        #print (stack)
        curr=queue.pop(0)
        res.append(curr.value)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
        
    return res 
    
 
class TreeNode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None 
```



# 
