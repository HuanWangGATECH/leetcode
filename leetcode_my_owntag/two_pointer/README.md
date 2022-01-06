# Grokking the coding interview 

# two pointer 

1. Dutch National Flag Problem
'''
Problem Statement 
Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers of the array as objects, 
hence, we can’t count 0s, 1s, and 2s to recreate the array.
The flag of the Netherlands consists of three colors: red, white and blue; 
and since our input array also consists of three different numbers that is why it is called Dutch National Flag problem.
Example 1:
Input: [1, 0, 2, 1, 0]
Output: [0 0 1 1 2]
Example 2:
Input: [2, 2, 0, 1, 2, 0]
Output: [0 0 1 2 2 2 ]
'''


https://leetcode.com/playground/jzDTXhta


# 2. Two sum using two pointers
'''
Problem Statement 
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.
Example 1:
Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6
Example 2:
Input: [2, 5, 9, 11], target=11
Output: [0, 2]
Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11
'''

https://leetcode.com/playground/R6xu8xYs

# 3. Qudropole sum to target (todo)

'''
Problem Challenge 1
Quadruple Sum to Target (medium) 
Given an array of unsorted numbers and a target number, find all unique quadruplets in it, whose sum is equal to the target number.
Example 1:
Input: [4, 1, 2, -1, 1, -3], target=1
Output: [-3, -1, 1, 4], [-3, 1, 1, 2]
Explanation: Both the quadruplets add up to the target.
Example 2:
Input: [2, 0, -1, 1, -2, 2], target=2
Output: [-2, 0, 2, 2], [-1, 0, 1, 2]
Explanation: Both the quadruplets add up to the target.
'''

# 4.Comparing Strings containing Backspaces (medium)

'''
Problem Challenge 2
Comparing Strings containing Backspaces (medium)
Given two strings containing backspaces (identified by the character ‘#’), check if the two strings are equal.
Example 1:
Input: str1="xy#z", str2="xzz#"
Output: true
Explanation: After applying backspaces the strings become "xz" and "xz" respectively.
Example 2:
Input: str1="xy#z", str2="xyz#"
Output: false
Explanation: After applying backspaces the strings become "xz" and "xy" respectively.
Example 3:
Input: str1="xp#", str2="xyz##"
Output: true
Explanation: After applying backspaces the strings become "x" and "x" respectively.
In "xyz##", the first '#' removes the character 'z' and the second '#' removes the character 'y'.
Example 4:
Input: str1="xywrrmp", str2="xywrrmu#p"
Output: true
Explanation: After applying backspaces the strings become "xywrrmp" and "xywrrmp" respectively.
'''


https://leetcode.com/playground/QRU6Yz2x

# 5. Minimum Window Sort 

'''
Problem Challenge 3
Minimum Window Sort (medium)
Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.
Example 1:
Input: [1, 2, 5, 3, 7, 10, 9, 12]
Output: 5
Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted
Example 2:
Input: [1, 3, 2, 0, -1, 7, 10]
Output: 5
Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted
Example 3:
Input: [1, 2, 3]
Output: 0
Explanation: The array is already sorted
Example 4:
Input: [3, 2, 1]
Output: 3
Explanation: The whole array needs to be sorted.
'''


#answer
import math


def shortest_window_sort(arr):
  low, high = 0, len(arr) - 1
  # find the first number out of sorting order from the beginning
  while (low < len(arr) - 1 and arr[low] <= arr[low + 1]):
    low += 1

  if low == len(arr) - 1:  # if the array is sorted
    return 0

  # find the first number out of sorting order from the end
  while (high > 0 and arr[high] >= arr[high - 1]):
    high -= 1

  # find the maximum and minimum of the subarray
  subarray_max = -math.inf
  subarray_min = math.inf
  for k in range(low, high+1):
    subarray_max = max(subarray_max, arr[k])
    subarray_min = min(subarray_min, arr[k])

  # extend the subarray to include any number which is bigger than the minimum of the subarray
  while (low > 0 and arr[low-1] > subarray_min):
    low -= 1
  # extend the subarray to include any number which is smaller than the maximum of the subarray
  while (high < len(arr)-1 and arr[high+1] < subarray_max):
    high += 1

  return high - low + 1


https://leetcode.com/playground/kDKsLRKg



# 6. Remove duplicates 

'''
Problem Statement 
Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in-place return the new length of the array.
Example 1:
Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].
Example 2:
Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after removing the duplicates will be [2, 11].
'''



https://leetcode.com/playground/BqFvRbSi

