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
Educative solution 

```python 
#answer
def find_subsets(nums):
  subsets = []
  # start by adding the empty subset
  subsets.append([])
  for currentNumber in nums:
    # we will take all existing subsets and insert the current number in them to create new subsets
    n = len(subsets)
    for i in range(n):
      # create a new subset from the existing subset and insert the current element to it
      set = subsets[i].copy()
      set.append(currentNumber)
      subsets.append(set)

  return subsets
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

# Subsets with duplicates 

'''
Problem Statement 

Given a set of numbers that might contain duplicates, find all of its distinct subsets.

Example 1:

Input: [1, 3, 3]

Output: [], [1], [3], [1,3], [3,3], [1,3,3]

Example 2:

Input: [1, 5, 3, 3]

Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3], [3,3], [1,3,3], [3,3,5], [1,5,3,3] 
'''

Solution 

This problem follows the Subsets pattern and we can follow a similar Breadth First Search (BFS) approach. The only additional thing we need to do is handle duplicates. Since the given set can have duplicate numbers, if we follow the same approach discussed in Subsets, we will end up with duplicate subsets, which is not acceptable. To handle this, we will do two extra things:

Sort all numbers of the given set. This will ensure that all duplicate numbers are next to each other.
Follow the same BFS approach but whenever we are about to process a duplicate (i.e., when the current and the previous numbers are same), instead of adding the current number (which is a duplicate) to all the existing subsets, only add it to the subsets which were created in the previous step.
Let’s take first Example mentioned below to go through each step of our algorithm:

Given set: [1, 5, 3, 3]  

Sorted set: [1, 3, 3, 5]

Start with an empty set: [[]]

Add the first number 1 to all the existing subsets to create new subsets: [[], [1]];

Add the second number 3 to all the existing subsets: [[], [1], [3], [1,3]].

The next number 3 is a duplicate. If we add it to all existing subsets we will get:

[[], [1], [3], [1,3], [3], [1,3], [3,3], [1,3,3]]

We got two duplicate subsets: [3], [1,3]  

Whereas we only needed the new subsets: [3,3], [1,3,3] 

To handle this instead of adding 3 to all the existing subsets, we only add it to the new subsets which were created in the previous 3rd step:

    [[], [1], [3], [1,3], [3,3], [1,3,3]]
    
Finally, add the forth number 5 to all the existing subsets: [[], [1], [3], [1,3], [3,3], [1,3,3], [5], [1,5], [3,5], [1,3,5], [3,3,5], [1,3,3,5]]


https://leetcode.com/playground/UQR3ysBZ


```python

def subsetsWithDuplicates(arr):
    
    res=[]
    res.append([])
    arr=sorted(arr)
    n=len(arr)
    startindex=0
    endindex=0
    for i in range(n):
        
        if i>0 and arr[i]==arr[i-1]:
            startindex=endindex 
            
        
        endindex=len(res)
        for j in range(startindex,endindex):
            res.append(res[j]+[arr[i]])
            
    return res 

def subsetsWithDuplicatesDFS(arr):
    res=[]
    
    dfs(arr,[],res)
    
    return res 
    
def dfs(arr,path,res):
    
    res.append(path)
    
    for i in range(len(arr)):
        if i >0 and arr[i]==arr[i-1]:
            continue 
        
        dfs(arr[i+1:],path+[arr[i]],res)
        
        
    
    
print (subsetsWithDuplicatesDFS([1,3,3,5]))
```


# Permutations (medium)

'''
Problem Statement 

Given a set of distinct numbers, find all of its permutations.

Permutation is defined as the re-arranging of the elements of the set. For example, {1, 2, 3} has the following six permutations:

{1, 2, 3}

{1, 3, 2}

{2, 1, 3}

{2, 3, 1}

{3, 1, 2}

{3, 2, 1}

If a set has ‘n’ distinct elements it will have n!n! permutations.

Example 1:

Input: [1,3,5]

Output: [1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]

'''

```python

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        
        res=[]
        
        self.dfs(nums,res,[])
        
        return res 
        
    def dfs(self,nums,res,path):
        
        if len(nums)==0:
            res.append(path)
        for i in range(len(nums)):
            
            self.dfs(nums[:i]+nums[i+1:],res,path+[nums[i]])
```


Permutation is defined as the re-arranging of the elements of the set. For example, {1, 2, 3} has the following six permutations:

{1, 2, 3}

{1, 3, 2}

{2, 1, 3}

{2, 3, 1}

{3, 1, 2}

{3, 2, 1}

If a set has ‘n’ distinct elements it will have n! permutations.

This problem follows the Subsets pattern and we can follow a similar Breadth First Search (BFS) approach. However, unlike Subsets, every permutation must contain all the numbers.


Let’s take the example mentioned below to generate all the permutations. Following a BFS approach, we will consider one number at a time:

If the given set is empty then we have only an empty permutation set: []

Let’s add the first element 1, the permutations will be: [1]

Let’s add the second element 3, the permutations will be: [3,1], [1,3]

Let’s add the third element 5, the permutations will be: [5,3,1], [3,5,1], [3,1,5], [5,1,3], [1,5,3], [1,3,5]

```python
def find_permutations(nums):
  numsLength = len(nums)
  result = []
  permutations = deque()
  permutations.append([])
  for currentNumber in nums:
    # we will take all existing permutations and add the current number to create new permutations
    n = len(permutations)
    for _ in range(n):
      oldPermutation = permutations.popleft()
      # create a new permutation by adding the current number at every position
      for j in range(len(oldPermutation)+1):
        newPermutation = list(oldPermutation)
        newPermutation.insert(j, currentNumber)
        if len(newPermutation) == numsLength:
          result.append(newPermutation)
        else:
          permutations.append(newPermutation)

  return result
 ```

# my BFS solution 

```python 
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        

        queue=[]
        queue.append([])
        for num in nums: 
            #print (num)
            for _ in range(len(queue)):
                current=queue.pop(0)
                n=len(current)        
                for i in range(n+1):
                    temp=current.copy()
                    temp.insert(i,num)
                    queue.append(temp)
                    
        return queue 
```



# String Permutations by changing case (medium)

'''
Problem Statement 

Given a string, find all of its permutations preserving the character sequence but changing case.

Example 1:

Input: "ad52"

Output: "ad52", "Ad52", "aD52", "AD52" 

Example 2:

Input: "ab7c"

Output: "ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"
'''


# BFS my approach 

```python
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        
        res=[]
        res.append('')
        
        for i in range(len(s)):
            
            letter=s[i]
            for _  in  range(len(res)):
                
                temp=res.pop(0)
                if letter.isalpha():
 
                    res.append(temp+letter.swapcase())
  
                res.append(temp+letter)
          
        return res 
```


# DFS my approach 


```pyhon 
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        res=[]
        
        def dfs(path,i):
            
            if len(path)==len(s):
                res.append(path)
                return 
            
            if s[i].isalpha():
                dfs(path+s[i].swapcase(),i+1)
            
            dfs(path+s[i],i+1)
            
        dfs('',0)
        
        
        return res 
```
