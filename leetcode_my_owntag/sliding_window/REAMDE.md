# Window sliding


# fruit into baskets 

'''
Problem Statement 

Given an array of characters where each character represents a fruit tree, you are given two baskets and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.

You can start with any tree, but once you have started you can’t skip a tree. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both the baskets.

Example 1:

Input: Fruit=['A', 'B', 'C', 'A', 'C']

Output: 3

Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

Example 2:

Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']

Output: 5

Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 

This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']

'''



Solution 

https://leetcode.com/playground/GfG78WTr



# Longest Subarray with Ones after Replacement (hard)

'''
Problem Statement 

Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.

Example 1:

Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2

Output: 6

Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.

Example 2:

Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3

Output: 9

Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.
'''


https://leetcode.com/playground/PegXyd7S


# Longest Substring with K Distinct Characters (medium)

'''
Problem Statement #

Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example 1:

Input: String="araaci", K=2

Output: 4

Explanation: The longest substring with no more than '2' distinct characters is "araa".

Example 2:

Input: String="araaci", K=1

Output: 2

Explanation: The longest substring with no more than '1' distinct characters is "aa".

Example 3:

Input: String="cbbebi", K=3

Output: 5

Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".

'''


my solution same as the first two questions 


# Longest Substring with Same Letters after Replacement (hard)

'''
Problem Statement 

Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.

Example 1:

Input: String="aabccbb", k=2

Output: 5

Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".

Example 2:

Input: String="abbcb", k=1

Output: 4

Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".

Example 3:

Input: String="abccde", k=1

Output: 3

Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".
'''


https://leetcode.com/playground/X2eySaji


# Maximum Sum Subarray of Size K (easy)

'''
Problem Statement #

Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.

Example 1:

Input: [2, 1, 5, 1, 3, 2], k=3 

Output: 9

Explanation: Subarray with maximum sum is [5, 1, 3].

Example 2:

Input: [2, 3, 4, 1, 5], k=2 

Output: 7

Explanation: Subarray with maximum sum is [3, 4].
'''


https://leetcode.com/playground/J2NXN7fJ

# No-repeat Substring (hard)

'''
Problem Statement 

Given a string, find the length of the longest substring which has no repeating characters.

Example 1:

Input: String="aabccbb"

Output: 3

Explanation: The longest substring without any repeating characters is "abc".

Example 2:

Input: String="abbbb"

Output: 2

Explanation: The longest substring without any repeating characters is "ab".

Example 3:

Input: String="abccde"

Output: 3

Explanation: Longest substrings without any repeating characters are "abc" & "cde".

'''


https://leetcode.com/playground/mauLVRJe

# Permutation in a String (hard)

'''
Problem Challenge 1

Permutation in a String (hard) 

Given a string and a pattern, find out if the string contains any permutation of the pattern.

Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:

abc

acb

bac

bca

cab

cba

If a string has ‘n’ distinct characters it will have n!n! permutations.

Example 1:

Input: String="oidbcaf", Pattern="abc"

Output: true

Explanation: The string contains "bca" which is a permutation of the given pattern.

Example 2:

Input: String="odicf", Pattern="dc"

Output: false

Explanation: No permutation of the pattern is present in the given string as a substring.

Example 3:

Input: String="bcdxabcdy", Pattern="bcdyabcdx"

Output: true

Explanation: Both the string and the pattern are a permutation of each other.

Example 4:

Input: String="aaacb", Pattern="abc"

Output: true

Explanation: The string contains "acb" which is a permutation of the given pattern.

'''

# Problem Challenge 2 - String Anagrams (hard) 

'''
Problem Challenge 2

String Anagrams (hard) 

Given a string and a pattern, find all anagrams of the pattern in the given string.

Anagram is actually a Permutation of a string. For example, “abc” has the following six anagrams:

abc

acb

bac

bca

cab

cba

Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

Example 1:

Input: String="ppqp", Pattern="pq"

Output: [1, 2]

Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".

Example 2:

Input: String="abbcabc", Pattern="abc"

Output: [2, 3, 4]

Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".
'''
# Problem Challenge 3 - Smallest Window containing Substring (hard)

'''
Problem Challenge 3

Smallest Window containing Substring (hard) 

Given a string and a pattern, find the smallest substring in the given string which has all the characters of the given pattern.

Example 1:

Input: String="aabdec", Pattern="abc"

Output: "abdec"

Explanation: The smallest substring having all characters of the pattern is "abdec"

Example 2:

Input: String="abdabca", Pattern="abc"

Output: "abc"

Explanation: The smallest substring having all characters of the pattern is "abc".

Example 3:

Input: String="adcad", Pattern="abc"


Output: ""

Explanation: No substring in the given string has all characters of the pattern.

'''
