# The XOR operator properties 

https://florian.github.io/xor-trick/




# Single number (easy)

'''
Problem Statement 

In a non-empty array of integers, every number appears twice except for one, find that single number.

Example 1:

Input: 1, 4, 2, 1, 3, 2, 3

Output: 4

Example 2:

Input: 7, 9, 7

Output: 9
'''


https://leetcode.com/playground/aMk6MmCt



```python 
def singleNumber(arr):
    res=0
    for i in range(len(arr)):
        res=res^arr[i]
        
        
    return res 
    
    
print (singleNumber([1,5,6,6,7,8,8,5,1]))
```
