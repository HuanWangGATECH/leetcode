From leetcode Heap data structure https://leetcode.com/explore/featured/card/heap/
# Introduction 
In many computer science applications, we only need to access the largest or smallest element in the dataset. We do not care about the order of other data in the data set. How do we efficiently access the largest or smallest element in the current dataset? The answer would be Heap.

In this Explore Card, we will introduce Heap. After reading this section, you will,

Have a better understanding of the “Heap” data structure and its implementation;

Have a better understanding of the concepts and methods of Max Heap and Min Heap;

Have a better understanding of Heap Sort;

Have a better understanding of the application scenarios of “Heap”;

Be able to use “Heap” in practice.

# Priority Queues
Before introducing a Heap, let's first talk about a Priority Queue.

Wikipedia: a priority queue is an abstract data type similar to a regular queue or stack data structure in which each element additionally has a "priority" associated with it. In a priority queue, an element with high priority is served before an element with low priority.

In daily life, we would assign different priorities to tasks, start working on the task with the highest priority and then proceed to the task with the second highest priority. This is an example of a Priority Queue.

A common misconception is that a Heap is the same as a Priority Queue, which is not true. A priority queue is an abstract data type, while a Heap is a data structure. Therefore, a Heap is not a Priority Queue, but a way to implement a Priority Queue.

There are multiple ways to implement a Priority Queue, such as array and linked list. However, these implementations only guarantee O(1)O(1) time complexity for either insertion or deletion, while the other operation will have a time complexity of O(N)O(N). On the other hand, implementing the priority queue with Heap will allow both insertion and deletion to have a time complexity of O(\log N)O(logN). So, what is a Heap?

In this chapter, we will learn to:

1. Understand the Heap data structure.

2. Understand Max Heap and Min Heap.

4. Understand the insertion and deletion of a Heap.

5. Implement a Heap.

# Definition of Heap
According to Wikipedia, a Heap is a special type of binary tree. A heap is a binary tree that meets the following criteria:

Is a complete binary tree;

The value of each node must be no greater than (or no less than) the value of its child nodes.

A Heap has the following properties:

Insertion of an element into the Heap has a time complexity of O(\log N)O(logN);

Deletion of an element from the Heap has a time complexity of O(\log N)O(logN);

The maximum/minimum value in the Heap can be obtained with O(1)O(1) time complexity.


# Classification of Heap
There are two kinds of heaps: Max Heap and Min Heap.

Max Heap: Each node in the Heap has a value no less than its child nodes. Therefore, the top element (root node) has the largest value in the Heap.

Min Heap: Each node in the Heap has a value no larger than its child nodes. Therefore, the top element (root node) has the smallest value in the Heap.



# Insertion and extraction (deletion) 

see in https://en.wikipedia.org/wiki/Binary_heap

# Implementation of heap using array

We often perform insertion, deletion, and getting the top element with a Heap data structure.

We can implement a Heap using an array. Elements in the Heap can be stored in the array in the form of a binary tree. The code below will implement “Max Heap” and “Min Heap” for integers (In LeetCode problems or daily work, we often will use existing libraries instead of manually implementing Heap).



```python 
# Implementing "Min Heap"
class MinHeap:
    def __init__(self, heapSize):
        # Create a complete binary tree using an array
        # Then use the binary tree to construct a Heap
        self.heapSize = heapSize
        # the number of elements is needed when instantiating an array
        # heapSize records the size of the array
        self.minheap = [0] * (heapSize + 1)
        # realSize records the number of elements in the Heap
        self.realSize = 0

    # Function to add an element
    def add(self, element):
        self.realSize += 1
        # If the number of elements in the Heap exceeds the preset heapSize
        # print "Added too many elements" and return
        if self.realSize > self.heapSize:
            print("Added too many elements!")
            self.realSize -= 1
            return
        # Add the element into the array
        self.minheap[self.realSize] = element
        # Index of the newly added element
        index = self.realSize
        # Parent node of the newly added element
        # Note if we use an array to represent the complete binary tree
        # and store the root node at index 1
        # index of the parent node of any node is [index of the node / 2]
        # index of the left child node is [index of the node * 2]
        # index of the right child node is [index of the node * 2 + 1]
        parent = index // 2
        # If the newly added element is smaller than its parent node,
        # its value will be exchanged with that of the parent node 
        while (self.minheap[index] < self.minheap[parent] and index > 1):
            self.minheap[parent], self.minheap[index] = self.minheap[index], self.minheap[parent]
            index = parent
            parent = index // 2
    
    # Get the top element of the Heap
    def peek(self):
        return self.minheap[1]
    
    # Delete the top element of the Heap
    def pop(self):
        # If the number of elements in the current Heap is 0,
        # print "Don't have any elements" and return a default value
        if self.realSize < 1:
            print("Don't have any element!")
            return sys.maxsize
        else:
            # When there are still elements in the Heap
            # self.realSize >= 1
            removeElement = self.minheap[1]
            # Put the last element in the Heap to the top of Heap
            self.minheap[1] = self.minheap[self.realSize]
            self.realSize -= 1
            index = 1
            # When the deleted element is not a leaf node
            while (index <= self.realSize // 2):
                # the left child of the deleted element
                left = index * 2
                # the right child of the deleted element
                right = (index * 2) + 1
                # If the deleted element is larger than the left or right child
                # its value needs to be exchanged with the smaller value
                # of the left and right child
                if (self.minheap[index] > self.minheap[left] or self.minheap[index] > self.minheap[right]):
                    if self.minheap[left] < self.minheap[right]:
                        self.minheap[left], self.minheap[index] = self.minheap[index], self.minheap[left]
                        index = left
                    else:
                        self.minheap[right], self.minheap[index] = self.minheap[index], self.minheap[right]
                        index = right
                else:
                    break
            return removeElement
    
    # return the number of elements in the Heap
    def size(self):
        return self.realSize
    
    def __str__(self):
        return str(self.minheap[1 : self.realSize + 1])
        

if __name__ == "__main__":
    	# Test cases
        minHeap = MinHeap(5)
        minHeap.add(3)
        minHeap.add(1)
        minHeap.add(2)
        # [1,3,2]
        print(minHeap)
        # 1
        print(minHeap.peek())
        # 1
        print(minHeap.pop())
        # 2
        print(minHeap.pop())
        # 3
        print(minHeap.pop())
        minHeap.add(4)
        minHeap.add(5)
        # [4,5]
        print(minHeap)
 ```
 ```python 
 # Implementing "Max Heap"
class MaxHeap:
    def __init__(self, heapSize):
        # Create a complete binary tree using an array
        # Then use the binary tree to construct a Heap
        self.heapSize = heapSize
        # the number of elements is needed when instantiating an array
        # heapSize records the size of the array
        self.maxheap = [0] * (heapSize + 1)
        # realSize records the number of elements in the Heap
        self.realSize = 0

    # Function to add an element
    def add(self, element):
        self.realSize += 1
        # If the number of elements in the Heap exceeds the preset heapSize
        # print "Added too many elements" and return
        if self.realSize > self.heapSize:
            print("Added too many elements!")
            self.realSize -= 1
            return
        # Add the element into the array
        self.maxheap[self.realSize] = element
        # Index of the newly added element
        index = self.realSize
        # Parent node of the newly added element
        # Note if we use an array to represent the complete binary tree
        # and store the root node at index 1
        # index of the parent node of any node is [index of the node / 2]
        # index of the left child node is [index of the node * 2]
        # index of the right child node is [index of the node * 2 + 1]
        parent = index // 2
        
        # If the newly added element is larger than its parent node,
        # its value will be exchanged with that of the parent node 
        while (self.maxheap[index] > self.maxheap[parent] and index > 1):
            self.maxheap[parent], self.maxheap[index] = self.maxheap[index], self.maxheap[parent]
            index = parent
            parent = index // 2
            
    # Get the top element of the Heap
    def peek(self):
        return self.maxheap[1]
    
    # Delete the top element of the Heap
    def pop(self):
        # If the number of elements in the current Heap is 0,
        # print "Don't have any elements" and return a default value
        if self.realSize < 1:
            print("Don't have any element!")
            return -sys.maxsize
        else:
            # When there are still elements in the Heap
            # self.realSize >= 1
            removeElement = self.maxheap[1]
            # Put the last element in the Heap to the top of Heap
            self.maxheap[1] = self.maxheap[self.realSize]
            self.realSize -= 1
            index = 1
            # When the deleted element is not a leaf node
            while (index <= self.realSize // 2):
                # the left child of the deleted element
                left = index * 2
                # the right child of the deleted element
                right = (index * 2) + 1
                # If the deleted element is smaller than the left or right child
                # its value needs to be exchanged with the larger value
                # of the left and right child
                if (self.maxheap[index] < self.maxheap[left] or self.maxheap[index] < self.maxheap[right]):
                    if self.maxheap[left] > self.maxheap[right]:
                        self.maxheap[left], self.maxheap[index] = self.maxheap[index], self.maxheap[left]
                        index = left
                    else:
                        self.maxheap[right], self.maxheap[index] = self.maxheap[index], self.maxheap[right]
                        index = right
                else:
                    break
            return removeElement
    
    # return the number of elements in the Heap
    def size(self):
        return self.realSize
    
    def __str__(self):
        return str(self.maxheap[1 : self.realSize + 1])
        

if __name__ == "__main__":
    	# Test cases
        maxHeap = MaxHeap(5)
        maxHeap.add(1)
        maxHeap.add(2)
        maxHeap.add(3)
        # [3,1,2]
        print(maxHeap)
        # 3
        print(maxHeap.peek())
        # 3
        print(maxHeap.pop())
        # 2
        print(maxHeap.pop())
        # 1
        print(maxHeap.pop())
        maxHeap.add(4)
        maxHeap.add(5)
        # [5,4]
        print(maxHeap)
 ```


# Common application of heap 

In most programming languages, Heaps are already built-in. Therefore, we usually do not need to implement a Heap from scratch. However, to use Heap adequately, we need to understand how Heap is commonly used.

In this chapter, we will learn how to:

Construct a Max Heap and a Min Heap.

Insert elements into a Heap.

Get the top element of a Heap.

Delete the top element from a Heap.

Get the length of a Heap.

Perform time and space complexity analysis for common applications that use a Heap.


# Construct a heap 


Constructing a Heap means initializing an instance of a Heap. All methods of Heap need to be performed on an instance. Therefore, we need to initialize an instance before applying the methods. When creating a Heap, we can simultaneously perform the heapify operation. Heapify means converting a group of data into a Heap.

Time complexity: O(N)O(N).

Space complexity: O(N)O(N).

```python
import heapq

# Construct an empty Min Heap
minHeap = []
heapq.heapify(minHeap)

# Construct an empty Max Heap
# As there are no internal functions to construct a Max Heap in Python,
# So, we will not construct a Max Heap.

# Construct a Heap with Initial values
# this process is called "Heapify"
# The Heap is a Min Heap
heapWithValues = [3,1,2]
heapq.heapify(heapWithValues)

# Trick in constructing a Max Heap
# As there are no internal functions to construct a Max Heap
# We can multiply each element by -1, then heapify with these modified elements.
# The top element will be the smallest element in the modified set,
# It can also be converted to the maximum value in the original dataset.
# Example
maxHeap = [1,2,3]
maxHeap = [-x for x in maxHeap]
heapq.heapify(maxHeap)
# The top element of maxHeap is -3
# Convert -3 to 3, which is the maximum value in the original maxHeap
```

# python heapq

Python Max Heap Video
Python's built-in heap module, heapq, differs from the standard implementation of a heap in two ways. Firstly, it uses zero-based indexing, and this means that it stores the root node at index zero instead of the size of the heap. As a result, the relationship between the index of the children and parent nodes is slightly different. Secondly, the built-in heapq module does not offer a direct way to create a max heap. Instead, we must modify the value(s) of each element when inserting it into the heap and when removing it from the heap. In the following video, we will learn more about this process. There are several benefits from implementing a heap in this way (you can read about them in the previous link).

# inserting an element 

Insertion means inserting a new element into the Heap. Note that, after the new element is inserted, properties of the Heap are still maintained.

Time complexity: O(\log N)O(logN)

Space complexity: O(1)O(1)

```python

# Insert an element to the Min Heap
heapq.heappush(minHeap, 5)

# Insert an element to the Max Heap
# Multiply the element by -1
# As we are converting the Min Heap to a Max Heap
heapq.heappush(maxHeap, -1 * 5)
```

# getting the top element of heap 

The top element of a Max heap is the maximum value in the Heap, while the top element of a Min Heap is the smallest value in the Heap. The top element of the Heap is the most important element in the Heap.

Time complexity: O(1)O(1).

Space complexity: O(1)O(1).

```python
# Get top element from the Min Heap
# i.e. the smallest element
minHeap[0]
# Get top element from the Max Heap
# i.e. the largest element
# When inserting an element, we multiplied it by -1
# Therefore, we need to multiply the element by -1 to revert it back
-1 * maxHeap[0]
```

# deleting top element 

Note that, after deleting the top element, the properties of the Heap will still hold. Therefore, the new top element in the Heap will be the maximum (for Max Heap) or minimum (for Min Heap) of the current Heap.

Time complexity: O(\log N)O(logN).

Space complexity: O(1)O(1).

```python 
# Delete top element from the Min Heap
heapq.heappop(minHeap)

# Delete top element from the Max Heap
heapq.heappop(maxHeap)
```

# getting the length of the heap 

The length of the Heap can be used to determine the size of the current heap, and it can also be used to determine if the current Heap is empty. If there are no elements in the current Heap, the length of the Heap is zero.

Time complexity: O(1)O(1)

Space complexity: O(1)O(1)

```python 
# Length of the Min Heap
len(minHeap)

# Length of the Max Heap
len(maxHeap)
```

# Space and time complexity 

| heap method              | time complexity | space complexity |
|--------------------------|-----------------|------------------|
| construct a heap         | O(n)            | O(n)             |
| insert an element        | O(logn)         | O(1)             |
| get the top element      | O(1)            | O(1)             |
| delete the top element   | O(logn)         | O(1)             |
| get the size of the heap | O(1)            | O(1)             |


# Complete code for minheap and maxheap 

```python
# Code for Min Heap
import heapq

# Create an array
minHeap = []

# Heapify the array into a Min Heap
heapq.heapify(minHeap)

# Add 3，1，2 respectively to the Min Heap
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 1)
heapq.heappush(minHeap, 2)

# Check all elements in the Min Heap, the result is [1, 3, 2]
print("minHeap: ", minHeap)

# Get the top element of the Min Heap
peekNum = minHeap[0]

# The result is 1
print("peek number: ", peekNum)

# Delete the top element in the Min Heap
popNum = heapq.heappop(minHeap)

# The result is 1
print("pop number: ", popNum)

# Check the top element after deleting 1, the result is 2
print("peek number: ", minHeap[0])

# Check all elements in the Min Heap, the result is [2,3]
print("minHeap: ", minHeap)

# Check the number of elements in the Min Heap
# Which is also the length of the Min Heap
size = len(minHeap)

# The result is 2
print("minHeap size: ", size)
```

```python
# Code for Max Heap
import heapq

# Create an array
maxHeap = []

# Heapify the array into a Min Heap
# we need to negate each element to convert the Min Heap to a Max Heap
heapq.heapify(maxHeap)

# Add 1，3，2 respectively to the Max Heap
# Note we are actually adding -1, -3 and -2 after negating the elements
# The Min Heap is now converted to a Max Heap
heapq.heappush(maxHeap, -1 * 1)
heapq.heappush(maxHeap, -1 * 3)
heapq.heappush(maxHeap, -1 * 2)

# Check all elements in the Max Heap, the result is [-3, -1, -2]
print("maxHeap: ", maxHeap)

# Check the largest element in the Heap, which is min value in the -1 * Heap
peekNum = maxHeap[0]

# The result is 3
print("peek number: ", -1 * peekNum)

# Delete the largest element in the Max Heap
# Which is the smallest value in the current Heap
popNum = heapq.heappop(maxHeap)

# The result is 3
print("pop number: ", -1 *  popNum)

# Check the largest element after deleting 3, the result is 2
print("peek number: ", -1 * maxHeap[0])

# Check all elements in the Max Heap, the result is [-2,-1]
print("maxHeap: ", maxHeap)

# Check the number of elements in the Max Heap
# Which is also the length of the Min Heap
size = len(maxHeap)

# The result is 2
print("maxHeap size: ", size)
```
