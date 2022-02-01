# The XOR operator properties 

https://florian.github.io/xor-trick/




# Single number (easy)

'''
Problem Statement 

In a non-empty array of integers, every number appears twice except for one, find that single number.

Example 1:

Input: 1, 4, 2, 1, 3, 2, 3

Output: 4

Example 2:

Input: 7, 9, 7

Output: 9
'''


https://leetcode.com/playground/aMk6MmCt



```python 
def singleNumber(arr):
    res=0
    for i in range(len(arr)):
        res=res^arr[i]
        
        
    return res 
    
    
print (singleNumber([1,5,6,6,7,8,8,5,1]))
```

# Complement of Base 10 Number (medium)

'''
Problem Statement 

Every non-negative integer N has a binary representation, for example, 8 can be represented as “1000” in binary and 7 as “0111” in binary.

The complement of a binary representation is the number in binary that we get when we change every 1 to a 0 and every 0 to a 1. For example, the binary 
complement of “1010” is “0101”.

For a given positive number N in base-10, return the complement of its binary representation as a base-10 integer.

Example 1:

Input: 8

Output: 7

Explanation: 8 is 1000 in binary, its complement is 0111 in binary, which is 7 in base-10.

Example 2:

Input: 10

Output: 5

Explanation: 10 is 1010 in binary, its complement is 0101 in binary, which is 5 in base-10.
'''

https://leetcode.com/playground/BGe2cYa6

```python 

import math 
def complementOf10Base(num):
    counter=0
    temp=num
    while temp>0:
        temp=temp>>1
        counter+=1
    
    allone=2**counter -1 
    
    return num^allone
    
    
    
print (complementOf10Base(8))
print (complementOf10Base(10))
```
