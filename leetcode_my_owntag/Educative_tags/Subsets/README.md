# Subsets (easy)

'''
Problem Statement 

Given a set with distinct elements, find all of its distinct subsets.

Example 1:

Input: [1, 3]

Output: [], [1], [3], [1,3]

Example 2:

Input: [1, 5, 3]

Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]

'''

https://leetcode.com/playground/new/empty

```python 
def subsets(arr):
    res=[]
    dfs(arr,res,[])
    return res 
    
def dfs(arr,res,path):
    res.append(path)
    for i in range(len(arr)):
        dfs(arr[i+1:],res,path+[arr[i]])
    
    
print (subsets([1,3]))
```
