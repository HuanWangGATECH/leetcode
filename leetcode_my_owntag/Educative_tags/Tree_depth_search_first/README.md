# All Paths for a Sum (medium)

'''
Problem Statement 

Given a binary tree and a number ‘S’, 

find all paths from root-to-leaf such that the sum of all the node values of each path equals ‘S’.

'''


https://leetcode.com/playground/aFG9wW2A


```python 
def allSumForPath(node,numSum):
    res=[]
    path=[]
    allSumForPathDFS(node,numSum,res,path)
    return path 
    
def allSumForPathDFS(node,numSum,res,path):
   
    if not node:
        return 
  
    res.append(node.value)
    if node.value==numSum and not node.left and not node.right: 
        path.append(list(res))

    else:
        allSumForPathDFS(node.left,numSum-node.value,res,path)
        allSumForPathDFS(node.right,numSum-node.value,res,path)

    del res[-1]


def allSumForPathIterative(node):
    res=[]
    stack=[]
    stack.append(node)

    while stack:
        curr=stack.pop()
        res.append(curr.value)
        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)
    return res



class TreeNode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None 
    

        
        
        
        
    

node1=TreeNode(1)
node2=TreeNode(2)
node3=TreeNode(3)
node4=TreeNode(4)
node5=TreeNode(5)

node1.left=node2
node1.right=node3
node2.left=node4
node4.right=node5 

print (allSumForPath(node1,4))

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(4)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
print (allSumForPath(root,23))

```


