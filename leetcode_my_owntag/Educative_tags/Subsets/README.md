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

To generate all subsets of the given set, we can use the Breadth First Search (BFS) approach. We can start with an empty set, iterate through all numbers one-by-one, and add them to existing sets to create new subsets.

Let’s take the example-2 mentioned above to go through each step of our algorithm:

Given set: [1, 5, 3]

Start with an empty set: [[]]

Add the first number 1 to all the existing subsets to create new subsets: [[],[1]];

Add the second number 5 to all the existing subsets: [[], [1], [5], [1,5]];

Add the third number 3 to all the existing subsets: [[], [1], [5], [1,5], [3], [1,3], [5,3], [1,5,3]].

Since the input set has distinct elements, the above steps will ensure that we will not have any duplicate subsets.


```python 

def subsetsBFS(arr):
    
    subsets=[]
    subsets.append([])

    for i in range(len(arr)):
        print (arr[i],subsets)
        for j in range(len(subsets)):
            subsets.append(subsets[j]+[arr[i]])
           
    return subsets


#print (subsets([1,3]))
print (subsetsBFS([1,3]))

```

And there is also a backtracing solution (recursive solution)


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
