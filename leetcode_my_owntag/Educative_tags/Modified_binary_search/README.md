# Agnostic binary search (easy)

'''
Problem Statement 

Given a sorted array of numbers, find if a given number ‘key’ is present in the array. Though we know that the array is sorted, we don’t know if it’s sorted in ascending or descending order. You should assume that the array can have duplicates.

Write a function to return the index of the ‘key’ if it is present in the array, otherwise return -1.

Example 1:

Input: [4, 6, 10], key = 10

Output: 2

Example 2:

Input: [1, 2, 3, 4, 5, 6, 7], key = 5

Output: 4

Example 3:

Input: [10, 6, 4], key = 10

Output: 0

Example 4:

Input: [10, 6, 4], key = 4

Output: 2
'''
https://leetcode.com/playground/Xg97QsSc

```python 
def agnosticBinarySearch(arr,target):
    # decreasing or increasing
    # duplicates 
    # empty 
    
    if len(arr)==0:
        return -1
        
    l,r=0,len(arr)-1
    if arr[r]>=arr[l]:
        booIncrease=True 
    else:
        booIncrease=False 
        
    while (l<=r):       
        m=(l+r)//2
        #print (l,m,r)
        if arr[m]==target:
            return m
        if booIncrease:
            if target<arr[m]:
                r=m-1
            else:
                l=m+1
        else:
            if target<arr[m]:
                l=m+1
            else:
                r=m-1
                
    return -1 

print (agnosticBinarySearch([4, 6, 10],10))

print (agnosticBinarySearch([1, 2, 3, 4, 5, 6, 7],5))

print (agnosticBinarySearch([10, 6, 4],10))
```
