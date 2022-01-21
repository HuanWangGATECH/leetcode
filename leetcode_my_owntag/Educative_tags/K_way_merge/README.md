# Merge K sorted list 

'''
Problem Statement 

Given an array of ‘K’ sorted LinkedLists, merge them into one sorted list.

Example 1:

Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4]

Output: [1, 2, 3, 3, 4, 6, 6, 7, 8]

Example 2:

Input: L1=[5, 8, 9], L2=[1, 7]

Output: [1, 5, 7, 8, 9]
'''

https://leetcode.com/playground/nzfUGKKq

```python
from heapq import *
def mergeKSortedLL(lists):
    minHeap=[]
    for item in lists:
        heappush(minHeap,item)
    dummyNode=Node(0)
    prev=dummyNode 
    while minHeap:  
        curr=heappop(minHeap)
        prev.next=curr
        if curr.next:
            heappush(minHeap,curr.next)
        prev=curr    
    
    return dummyNode.next 


# solution 

def merge_lists(lists):
     minHeap = []

     # put the root of each list in the min heap
    for root in lists:
        if root is not None:
             heappush(minHeap, root)

  # take the smallest(top) element form the min-heap and add it to the result
  # if the top element has a next element add it to the heap
    resultHead, resultTail = None, None
    while minHeap:
        node = heappop(minHeap)
        if resultHead is None:
            resultHead = resultTail = node
        else:
            resultTail.next = node
            resultTail = resultTail.next

        if node.next is not None:
            heappush(minHeap, node.next)

        return resultHead


class Node:
    
    def __init__(self,value):
        self.value=value
        self.next=None 
        
        # used for the min-heap
    def __lt__(self, other):
        return self.value < other.value 
        
def main():        
    l1 = Node(2)
    l1.next = Node(6)
    l1.next.next = Node(8)

    l2 = Node(3)
    l2.next = Node(6)
    l2.next.next = Node(7)

    l3 = Node(1)
    l3.next = Node(3)
    l3.next.next = Node(4)

    result = mergeKSortedLL([l1, l2, l3])
    
    
    while result != None:
        print(str(result.value) + " ", end='')
        result = result.next

    
main()


```

# Kth smallest number in M sorted lists (medium)

'''
Problem Statement  

Given ‘M’ sorted arrays, find the K’th smallest number among all the arrays.

Example 1:

Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4], K=5

Output: 4

Explanation: The 5th smallest number among all the arrays is 4, this can be verified from the merged 

list of all the arrays: [1, 2, 3, 3, 4, 6, 6, 7, 8]

Example 2:

Input: L1=[5, 8, 9], L2=[1, 7], K=3

Output: 7

Explanation: The 3rd smallest number among all the arrays is 7.
'''


https://leetcode.com/playground/naHtbh4X
