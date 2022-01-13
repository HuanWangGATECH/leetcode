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


'''python
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
'''