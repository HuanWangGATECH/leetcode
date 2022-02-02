# Reverse alternating K-element Sub-list (medium) 


'''
Problem Challenge 1

Reverse alternating K-element Sub-list (medium)


Given the head of a LinkedList and a number ‘k’, reverse every alternating ‘k’ sized sub-list starting from the head.


If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.

'''


https://leetcode.com/playground/PHuX6kdT



# Rotate a linked list (medium)

'''
Problem Challenge 2

Rotate a LinkedList (medium)

Given the head of a Singly LinkedList and a number ‘k’, rotate the LinkedList to the right by ‘k’ nodes.
'''

https://leetcode.com/playground/i9d3fLH6

```python
  def rotateLinkedList(head,k):
    
    current=head
    length=0
    while current:
        current=current.next
        length+=1 
    
    k=k%length
    
    #print (length,k)
    counter=1
    khead=None
    ktail=None
    kheadprev=None
    current=head
    prev=None
    while current:
        #print (current.val)
        if counter==(length-k+1): 
            khead=current
            kheadprev=prev
            print (khead.val)
        if counter==length:
            ktail=current
            print (ktail.val)
        counter+=1 
        temp=current.next
        prev=current
        current=temp 
        
    kheadprev.next=None 
    ktail.next=head
    
    return khead
```

