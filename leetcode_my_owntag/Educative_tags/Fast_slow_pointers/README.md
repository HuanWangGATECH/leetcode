# Happy Number (medium)
'''
Problem Statement 

Any number will be called a happy number if, 

after repeatedly replacing it with a number equal to the sum of the square of all of its digits, 

leads us to number ‘1’. All other (not-happy) numbers will never reach ‘1’. 

Instead, they will be stuck in a cycle of numbers which does not include ‘1’.
'''


https://leetcode.com/playground/hJNDWh52


# Linked list cycle (easy)

'''
Problem Statement 

Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.
'''


https://leetcode.com/playground/M3YSnpWf


# Middle of linked list (easy)

'''
Problem Statement 

Given the head of a Singly LinkedList, write a method to return the middle node of the LinkedList.

If the total number of nodes in the LinkedList is even, return the second middle node.

Example 1:

Input: 1 -> 2 -> 3 -> 4 -> 5 -> null

Output: 3

Example 2:

Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null

Output: 4

Example 3:

Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> null

Output: 4
'''


https://leetcode.com/playground/jRD9nxqy


```python 
  def midLinkedList(head):
      slow=head
      fast=head
      while fast and fast.next:
        
          slow=slow.next
          fast=fast.next.next 
        
      return slow.value 
    
    


    
  class Node:
      def __init__(self,value=None):
          self.value=value 
          self.next=None 
        
        
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print (midLinkedList(head))


  head.next.next.next.next.next = Node(6)

  print (midLinkedList(head))
```

# Problem Challenge 1 - Palindrome LinkedList (medium)

'''
Problem Challenge 1

Palindrome LinkedList (medium)

Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.

Your algorithm should use constant space and the input LinkedList should be in the original form once the algorithm is finished. The algorithm should have 

O(N)O(N) time complexity where ‘N’ is the number of nodes in the LinkedList.

Example 1:

Input: 2 -> 4 -> 6 -> 4 -> 2 -> null

Output: true

Example 2:

Input: 2 -> 4 -> 6 -> 4 -> 2 -> 2 -> null

Output: false
'''

https://leetcode.com/playground/Jero3bdc

```python 
def palindromeLinkedList(head):
    
    slow=head
    fast=head
   
    while fast and fast.next:
        #print (slow.value,fast.value)
        slow=slow.next
        fast=fast.next.next
    
    
    # slow is the middle of the linked list 
    # reverse linked list starting from slow and get its head 
    reSecondHalfHead=reverseLinkedList(slow)
    
    
    
    while head and reSecondHalfHead:
        if head.value!=reSecondHalfHead.value:
            return False
        head=head.next
        reSecondHalfHead=reSecondHalfHead.next 
        
    return True 
    
    
def reverseLinkedList(head):
    prev=None 
    curr=head
    while curr:
        temp=curr.next
        curr.next=prev
        prev=curr
        curr=temp 
        
        
    return prev


def printLinkedList(head):
    
    while head:
        print (head.value)
        head=head.next
    
    
    
class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None 
        

        
        
head = Node(2)
head.next = Node(4)
head.next.next = Node(6)
head.next.next.next = Node(4)
head.next.next.next.next = Node(2)


#print (reverseLinkedList(node1).value)
#printLinkedList(node1)
print (palindromeLinkedList(head))
```


# Problem Challenge 2 - Rearrange a LinkedList (medium)

'''
Problem Challenge 2

Rearrange a LinkedList (medium)

Given the head of a Singly LinkedList, write a method to modify the LinkedList such that the nodes from the second half of the LinkedList are inserted alternately to the nodes from the first half in reverse order. So if the LinkedList has nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null, your method should return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.

Your algorithm should not use any extra space and the input LinkedList should be modified in-place.

Example 1:

Input: 2 -> 4 -> 6 -> 8 -> 10 -> 12 -> null

Output: 2 -> 12 -> 4 -> 10 -> 6 -> 8 -> null 

Example 2:

Input: 2 -> 4 -> 6 -> 8 -> 10 -> null

Output: 2 -> 10 -> 4 -> 8 -> 6 -> null
'''


# Problem Challenge 3 - Cycle in a Circular Array (hard)

'''
Problem Challenge 3

Cycle in a Circular Array (hard)

We are given an array containing positive and negative numbers. Suppose the array contains a number ‘M’ at a particular index. 

Now, if ‘M’ is positive we will move forward ‘M’ indices and if ‘M’ is negative move backwards ‘M’ indices. You should assume that the array is circular which means two things:

If, while moving forward, we reach the end of the array, we will jump to the first element to continue the movement.

If, while moving backward, we reach the beginning of the array, we will jump to the last element to continue the movement.

Write a method to determine if the array has a cycle. The cycle should have more than one element and should follow one direction which means the cycle should not contain both forward and backward movements.

Example 1:

Input: [1, 2, -1, 2, 2]

Output: true

Explanation: The array has a cycle among indices: 0 -> 1 -> 3 -> 0

Example 2:

Input: [2, 2, -1, 2]

Output: true

Explanation: The array has a cycle among indices: 1 -> 3 -> 1

Example 3:

Input: [2, 1, -1, -2]

Output: false

Explanation: The array does not have any cycle.
'''


# Start of LinkedList Cycle (medium)

'''
Problem Statement 

Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.

'''
https://leetcode.com/playground/3CyAYvpR


```python
def find_cycle_start(head):
    cycle_length = 0
  # find the LinkedList cycle
    slow, fast = head, head
    while (fast is not None and fast.next is not None):
        fast = fast.next.next
        slow = slow.next
        if slow == fast:  # found the cycle
            cycle_length = calculate_cycle_length(slow)
            break
    return find_start(head, cycle_length)


def calculate_cycle_length(slow):
    current = slow
    cycle_length = 0
    while True:
        current = current.next
        cycle_length += 1
        if current == slow:
        break
    return cycle_length


def find_start(head, cycle_length):
    pointer1 = head
    pointer2 = head
    # move pointer2 ahead 'cycle_length' nodes
    while cycle_length > 0:
        pointer2 = pointer2.next
        cycle_length -= 1
    # increment both pointers until they meet at the start of the cycle
    while pointer1 != pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1

    
    

    
class node:
    
    def __init__(self,value):
        
        self.value=value
        self.next=None 
        


head=node(1)
head.next=node(2)
head.next.next=node(3)
head.next.next.next=node(4)
head.next.next.next.next=head.next

print (findCycleStart(head))


    
    
    

```
