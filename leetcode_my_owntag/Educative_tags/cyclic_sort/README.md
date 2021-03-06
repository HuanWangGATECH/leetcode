# Cyclic sort 
'''
Problem Statement 

We are given an array containing ‘n’ objects. Each object, when created, was assigned a unique number from 1 to ‘n’ based on their creation sequence. 

This means that the object with sequence number ‘3’ was created just before the object with sequence number ‘4’.

Write a function to sort the objects in-place on their creation sequence number in O(n) and without any extra space. 

For simplicity, let’s assume we are passed an integer array containing only the sequence numbers, though each number is actually an object.

Example 1:

Input: [3, 1, 5, 4, 2]

Output: [1, 2, 3, 4, 5]

Example 2:

Input: [2, 6, 4, 3, 1, 5]

Output: [1, 2, 3, 4, 5, 6]

Example 3:

Input: [1, 5, 6, 4, 3, 2]

Output: [1, 2, 3, 4, 5, 6]

'''

https://leetcode.com/playground/XByUm5kR

```python 
def cyclicSort(arr):
    n=len(arr)
    for i in range(n):
        
        arr[arr[i]-1],arr[i]=arr[i],arr[arr[i]-1]
    
    return arr 
    


def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
        i += 1
    return nums    
    
print (cyclicSort([3, 1, 5, 4, 2]))
```
# Find all duplicate numberw 

'''
Problem Statement 

We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’.

The array has some duplicates, find all the duplicate numbers without using any extra space.

Example 1:

Input: [3, 4, 4, 5, 5]

Output: [4, 5]

Example 2:

Input: [5, 4, 7, 2, 3, 5, 3]

Output: [3, 5]
'''
https://leetcode.com/playground/new/empty

```python 
def find_all_duplicates(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1
    print (nums)
    
    
    duplicateNumbers = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            duplicateNumbers.append(nums[i])

    return duplicateNumbers



print (find_all_duplicates([3, 4, 4, 5, 5]))

print (find_all_duplicates([8,8,7,7,6,6,2,3]))
```
