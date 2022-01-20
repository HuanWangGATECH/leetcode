# k smallest number 

'''
Problem Statement 

Given an unsorted array of numbers, find Kth smallest number in it.

Please note that it is the Kth smallest number in the sorted order, not the Kth distinct element.

Note: For a detailed discussion about different approaches to solve this problem, take a look at Kth Smallest Number.

Example 1:

Input: [1, 5, 12, 2, 11, 5], K = 3

Output: 5

Explanation: The 3rd smallest number is '5', as the first two smaller numbers are [1, 2].

Example 2:

Input: [1, 5, 12, 2, 11, 5], K = 4

Output: 5

Explanation: The 4th smallest number is '5', as the first three small numbers are [1, 2, 5].

Example 3:

Input: [5, 12, 11, -1, 12], K = 3

Output: 11

Explanation: The 3rd smallest number is '11', as the first two small numbers are [5, -1].
'''

```python
#answer
from heapq import *


def find_Kth_smallest_number(nums, k):
  maxHeap = []
  # put first k numbers in the max heap
  for i in range(k):
    heappush(maxHeap, -nums[i])

  # go through the remaining numbers of the array, if the number from the array is smaller than the
  # top(biggest) number of the heap, remove the top number from heap and add the number from array
  for i in range(k, len(nums)):
    if -nums[i] > maxHeap[0]:
      heappop(maxHeap)
      heappush(maxHeap, -nums[i])

  # the root of the heap has the Kth smallest number
  return -maxHeap[0]

```

# Top K numbers (easy)


'''
Problem Statement 

Given an unsorted array of numbers, find the ‘K’ largest numbers in it.

Note: For a detailed discussion about different approaches to solve this problem, take a look at Kth Smallest Number.

Example 1:

Input: [3, 1, 5, 12, 2, 11], K = 3

Output: [5, 12, 11]

Example 2:

Input: [5, 12, 11, -1, 12], K = 3

Output: [12, 11, 12]
'''


https://leetcode.com/playground/HC2YHXQ5


```python
from heapq import *
def topKNumber(arr,k):
    res=[]
    heapify(res)
    
    for i in range(len(arr)):
        heappush(res,-arr[i])
        
    print (res)    
    results=[]
    for i in range(k):
        results.append(-heappop(res))
    
    
    return results 

def topKNumberAp2(arr,k):
    
    res=[]
    
    for i in range(k):
        heappush(res,arr[i])
        
    for i in range(k,len(arr)):
        if arr[i] > res[0]:
            heappop(res)
            heappush(res,arr[i])
    
    return res 
            
        
    
print (topKNumber([3, 1, 5, 12, 2, 11],3))
print (topKNumberAp2([3, 1, 5, 12, 2, 11],3))
```
