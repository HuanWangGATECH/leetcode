# Find the medium of a number stream (medium)

'''
Problem Statement 

Design a class to calculate the median of a number stream. The class should have the following two methods:

insertNum(int num): stores the number in the class

findMedian(): returns the median of all numbers inserted in the class

If the count of numbers inserted in the class is even, the median will be the average of the middle two numbers.

Example 1:
1. insertNum(3)

2. insertNum(1)

3. findMedian() -> output: 2

4. insertNum(5)

5. findMedian() -> output: 3

6. insertNum(4)

7. findMedian() -> output: 3.5
'''


# https://leetcode.com/playground/htLiAF2j

```python 
import heapq 
class Stream:
    
    def __init__(self):
        self.minheap=[]
        heapq.heapify(self.minheap)
        self.maxheap=[]
        heapq.heapify(self.maxheap)
        self.median=None 
        
    def insertNums(self,num=None):
    
        
        if num:
            if len(self.maxheap)==0 or num<=self.maxheap[0]:
                heapq.heappush(self.maxheap,-num)
            else:
                heapq.heappush(self.minheap,num)
        
        if len(self.maxheap)+1 <len(self.minheap):
            heapq.heappush(self.maxheap,-heapq.heappop(self.minheap))
        
            
        print (self.minheap,self.maxheap)
            
            
    def findMedian(self):
        
        if len(self.minheap)==len(self.maxheap):
            print (self.minheap[0],-self.maxheap[0])
            return float((self.minheap[0]-self.maxheap[0])/2)
            
        else:
            return self.maxheap[0]
        
        
        
        
stream1=Stream()
stream1.insertNums(1)
stream1.insertNums(2)
stream1.insertNums(3)
stream1.insertNums(4)
print (stream1.findMedian())

stream1=Stream()
stream1.insertNums(8)
stream1.insertNums(4)
stream1.insertNums(10)
stream1.insertNums(7)
print (stream1.findMedian())
```
