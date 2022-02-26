# This link below is hugely helpful!

https://leetcode.com/problems/binary-search/discuss/423162/Binary-Search-101

Binary search is often a topic that's easy to be explained in the abstract level, but when it comes to write bug free implementations, it's rather difficult.

Some of the most common problems include:

Infinity loop
Can't decide where to shrink
Do I use lo or hi
When to exit the loop
...
In this article, I will be sharing my insights on how to write bug free binary search with just a little pattern.

If you are familiar with binary search and just want to see the pattern, you can go directly to the part: The Pattern.

What is binary search?
Normally, to find the target in a group, such as an array of numbers, the worst case scenario is we need to go through every single element (O(n)). However, when these elements are sorted, we are able to take the privilege of this extra information to bring down the search time to O(log n), that is if we have 100 elements, the worst case scenario would be 10 searches. That is a huge performance improvement.

The Gif below demonstrates the power of binary search.




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


# Bitonic Array Maximum (easy)

https://leetcode.com/problems/find-peak-element/


'''
Problem Statement 

Find the maximum value in a given Bitonic array. An array is considered bitonic if it is monotonically increasing and then monotonically decreasing. 

Monotonically increasing or decreasing means that for any index i in the array arr[i] != arr[i+1].

Example 1:

Input: [1, 3, 8, 12, 4, 2]

Output: 12

Explanation: The maximum number in the input bitonic array is '12'.

Example 2:

Input: [3, 8, 3, 1]

Output: 8

Example 3:

Input: [1, 3, 8, 12]

Output: 12

Example 4:

Input: [10, 9, 8]

Output: 10
'''


```python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
 
        while l < r:
            
            m=(l+r)>>1
            
            if nums[m]>nums[m+1]:
                r=m
            else:
                l=m+1
        
        return l 
```


# Ceiling of a Number (medium)

'''
Problem Statement #

Given an array of numbers sorted in an ascending order, find the ceiling of a given number ‘key’. The ceiling of the ‘key’ will be the smallest element in the 

given array greater than or equal to the ‘key’.

Write a function to return the index of the ceiling of the ‘key’. If there isn’t any ceiling return -1.

Example 1:

Input: [4, 6, 10], key = 6

Output: 1

Explanation: The smallest number greater than or equal to '6' is '6' having index '1'.

Example 2:

Input: [1, 3, 8, 10, 15], key = 12

Output: 4

Explanation: The smallest number greater than or equal to '12' is '15' having index '4'.

Example 3:

Input: [4, 6, 10], key = 17

Output: -1

Explanation: There is no number greater than or equal to '17' in the given array.

Example 4:

Input: [4, 6, 10], key = -1

Output: 0

Explanation: The smallest number greater than or equal to '-1' is '4' having index '0'.
'''


https://leetcode.com/playground/6Yq3zJF4



# Minimum difference element ( medium) 

'''




Problem Statement 

Given an array of numbers sorted in ascending order, 

find the element in the array that has the minimum difference with the given ‘key’.

Example 1:

Input: [4, 6, 10], key = 7

Output: 6

Explanation: The difference between the key '7' and '6' is minimum than any other number in the array 

Example 2:

Input: [4, 6, 10], key = 4

Output: 4

Example 3:

Input: [1, 3, 8, 10, 15], key = 12

Output: 10

Example 4:

Input: [4, 6, 10], key = 17

Output: 10
'''


https://leetcode.com/playground/UVytp3nV
