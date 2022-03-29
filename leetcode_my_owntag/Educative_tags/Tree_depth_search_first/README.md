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




# in order traversal of tree 

https://www.techiedelight.com/inorder-tree-traversal-iterative-recursive/


## recursive approach 
```python
# Data structure to store a binary tree node
class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
 
# Recursive function to perform inorder traversal on the tree
def inorder(root):
 
    # return if the current node is empty
    if root is None:
        return
 
    # Traverse the left subtree
    inorder(root.left)
 
    # Display the data part of the root (or current node)
    print(root.data, end=' ')
 
    # Traverse the right subtree
    inorder(root.right)
 
 
if __name__ == '__main__':
 
    ''' Construct the following tree
               1
             /   \
            /     \
           2       3
          /      /   \
         /      /     \
        4      5       6
              / \
             /   \
            7     8
    '''
 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
 
    inorder(root)
```

## iterative approach 

```python
from collections import deque
 
 
# Data structure to store a binary tree node
class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
 
# Iterative function to perform inorder traversal on the tree
def inorderIterative(root):
 
    # create an empty stack
    stack = deque()
 
    # start from the root node (set current node to the root node)
    curr = root
 
    # if the current node is None and the stack is also empty, we are done
    while stack or curr:
 
        # if the current node exists, push it into the stack (defer it)
        # and move to its left child
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            # otherwise, if the current node is None, pop an element from the stack,
            # print it, and finally set the current node to its right child
            curr = stack.pop()
            print(curr.data, end=' ')
 
            curr = curr.right
 
 
if __name__ == '__main__':
 
    ''' Construct the following tree
               1
             /   \
            /     \
           2       3
          /      /   \
         /      /     \
        4      5       6
              / \
             /   \
            7     8
    '''
 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
 
    inorderIterative(root)
 ```
 
 


