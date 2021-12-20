# See questions here https://algo.monster/problems/google_online_assessment_questions


## 1 Compare Strings

https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/

A string is defined to be "strictly smaller" than another string when the number of occurrences of the lexicographically smallest character in the string is less than that of the other. For example, "abcd" is strictly smaller than "aaa" because the smallest character in "abcd", "a", appears 1 time, whereas the smallest character in "aaa", "a", appears 3 times.

In another example, "d" is strictly smaller than "ff" because the smallest character in "d", 'd', appears 1 time, and the smallest character in "ff", 'f', appears 2 times.

Given a list of strings str1 with m elements, and another list of strings str2 with n elements, return an array A of n integers. For 0 <= i < n, A[i] is the number of strings in str1 that are strictly smaller than the comparison i-th string in str2. Focus on correctness instead of performance in your solution.

Input

str1: a list of strings with m elements.
str2: a list of strings with n elements.

Output

An integer array of size n

Examples

Example 1:
Input:

str1 = "abcd aabc bd"
str2 = "aaa aa"
Output: [3, 2]

Explanation:

All the strings in str1 are strictly smaller than "aaa", and strings "abcd" and "bd" are strictly smaller than "aa".

Constraints

1 <= n, m <= 10000
1 <= length of any string in str1 or str2 <= 10
All the input strings are made up of lowercase English alphabets (a-z)


A good solution 

  class Solution:
      def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
          # 1. Capture counts of smallest characters in each word, and sort 
          # the list in ascending order.
          W = sorted([w.count(min(w)) for w in words])
        
          res = []
          for q in queries:
              # 2. Perform binary search of smallest characters in each query
              # against the sorted list from step#1.
              cnt = q.count(min(q))
              idx = bisect.bisect(W, cnt)
              res.append(len(words) - idx)
          return res

## 2 largest subarray 


https://www.geeksforgeeks.org/greatest-contiguous-sub-array-of-size-k/


An array A is greater than an array B if the first non-matching item in both arrays has a greater value in A than in B. For example,

A = [3, 4, 9, 6, 8]
B = [3, 4, 8, 6, 7]
A is bigger than B because the first non-matching element is larger in A (A[2] > B[2]).

A contiguous subarray is a subarray that has consecutive indexes.

Given an array arr consisting of n integers and an integer k, return the largest contiguous subarray of length k from all the possible contiguous subarrays of length k.

Constraints

1 <= k <= n <= 100
1 <= arr[i] <= 1000

Examples

Example 1:
Input:
arr = [1, 4, 3, 2, 5]

k = 4

Output: [4, 3, 2, 5]
Explanation:
There are 2 possible subarrays of size 4: [1, 4, 3, 2] and [4, 3, 2, 5], and the largest subarray is [4, 3, 2, 5].

## 3 maximum area serving pizza /cake 

https://leetcode.com/discuss/interview-question/348510/Google-or-OA-2019-or-Maximum-Area-Serving-Cake

Given an array of positive integers representing the radii of circular pizzas and the number of guests at a movie party, return the size of the largest piece of pizza (rounded to 4 decimal places) that can be cut so that every guest gets a slice of pizza with the same size. It is not possible that a single slice has some part of one pizza and some part of another pizza, and each guest gets only once slice of pizza.

Constraints:

1 <= number of pizzas <= 1000
1 <= radii[i] <= 1000
1 <= number of guests <= 1000

Examples

Example 1:
Input:
radii = [1, 1, 1, 2, 2, 3]

guests = 6

Output: 7.0686

Explanation:

You can divide the pizza with a radius of 3 by 4: area 28.743 / 4 = 7.0686 to get 4 slices. Get the remaining 2 slices from the pizzas wth radius 2 because they have an area larger than 7.0686.

Example 2:
Input:
radii = [4, 3, 3]

guests = 3

Output: 28.2743
Example 3:
Input:
radii = [6, 7]

guests = 12

Output: 21.9911


## 4 Minimum Number of Decreasing Subsequence Partitions

https://edydfang.com/2019/11/19/longest-increasing-subsequence-problem-and-its-duality/

https://www.geeksforgeeks.org/minimum-number-of-increasing-subsequences/

Given an integer array, split it into strictly decreasing subarrays. Return the minimum number of decreasing subarrays you can get from splitting the array.

Examples
Example 1:
Input:
[5, 2, 4, 3, 1, 7]

Output: 3
Explanation:
The array can be split into [5, 2, 1], [4, 3], [7] to get 3 decreasing subarrays. Or it can be split into [5, 4, 3], [2, 1], [7] to also get 3 decreasing subarrays.

The partition of [5, 4, 3, 2, 1], [7] is not valid because [5, 4, 3, 2, 1] is not a subarray of the original array.

Example 2:
Input:
[2, 9, 13, 14, 4, 8, 7, 6, 10]

Output: 4
Explanation:
[2], [9, 4], [13, 10], [14, 8, 7, 6]

Example 3:
Input:
[6, 6, 6]

Output: 3
Explanation:
[6], [6], [6]

## 5 Pick Up Coupons

You are given a scratchcard consists of a row of non-negative integers. To win the scratch game, you need to scratch at least 2 numbers of the same value. You can only scratch consecutive numbers from the card. Scratching each number costs 1 dollar. Return the minimum cost to win the game, or -1 if winning is not possible.

Examples
Example 1:
Input:
[1, 3, 4, 2, 3, 4, 5]

Output: 4
Explanation:
You can scratch either [3, 4, 2, 3] or [4, 2, 3, 4].

Example 2:
Input:
[2, 5, 0, 3, 7]

Output: -1
Explanation:
There are no numbers of the same value.

## 6 Rose garden/onion picking

You are planting onions to make salads. Given an array of positive integers that indicates the day that each of your onion is ready for harvest, the minimum number of adjacent mature onions required for a salad, and the number of salads you want to make, return the earliest day that you can finish making all salads. If it is impossible to make the required number of salads, return -1.

Input
onions: an array of positive integers. Onion i will be ready for harvest on day onions[i].
k: the minimum number of adjacent onions required to make a salad.
n: the number of salads you want to make.
Output
Return the earliest day that you can finish making n salads, or -1 if the task is impossible.

Examples
Example 1:
Input:

onions = [1, 2, 6, 10, 3, 4, 1]
k = 2
n = 2
Output: 4

Explanation:

Day 1: [h, o, o, o, o, o, h]

The first and last onions are ready for harvest.

Day 2: [h, h, o, o, o, o, h]

The second onion matures, and the first 2 mature onions can be used to make a salad.

Day 3: [h, h, o, o, h, o, h]

Day 4: [h, h, o, o, h, h, h]

The last 3 onions make a salad, meeting the required n = 2 salads. So day 4 is the earliest day to finish making the required number of salads.

Constraints

1 <= onions.length == 10^5
1 <= onions[i] <= 10^9
1 <= n <= 10^6
1 <= k <= onions.length

## 7 smallest integer satisfying the rule 

You have a number written down on a piece of paper. Unfortunately, you are extremely clumsy and you knocked over a bottle of ink, which covered the paper. This causes some numbers to be completely illegible.

This number is very important to you, so you want to reconstruct the number. You don't remember the original number, but you distinctly remember that this number has two peculiar attributes: it has no zeros anywhere in the number, and each adjacent digits are distinct. With this information, it is not necessarily possible to guarantee a number, so you just want to find the lowest possible number given the current information.

Parameter

digits: A string of length n consisting of 1 ~ 9 and/or ? (which represents an illegible digit).
Result
A string representing the lowest possible number that satisfy the conditions described above.
Examples
Example 1
Input: digits = "1??13"

Output: "12313"

Example 2
Input: digits = "?1???2??3???4?"

Output: "21213212312141"

Constraints:

1 <= n <= 2000

## 8 water plants / soup 

You work in a restaurant and is tasked to fill some bowls with soup in a big stock pot. The bowls are positioned in a row, and you are going to fill the bowls with a large ladle. To avoid mistakes, you have decided to:

Fill the bowls from left to right;
Fill each bowl if you have enough soup for it, otherwise refill the ladle with more soup;
Fill each bowl in one go without taking a break to refill the ladle. This means that you may sometimes have to refill your ladle before or after filling a bowl, even though the ladle isn't completely empty.
You start at the stock pot, which is positioned one step before the first bowl. How many steps will you take to finish filling all the bowls in the row? The bowls are positioned one step apart from each other.

Given an array of n integers representing the amount of soup required for each bowl and the ladle capacity, return the number of steps needed to fill all the bowls.

Constraints

1 <= n <= 1000
1 <= bowls[i] <= 10^6
1 <= capacity <= 10^9
The ladle is large enough to fully fill any bowl
Examples
Example 1:
Input:
bowls = [2, 4, 5, 1, 2]

capacity = 6

Output: 17
Explanation:

First, you fill bowl 0 and 1 - 2 steps. Then, you go back and refill - 2 steps - and fill bowl 2 and 3 - 4 steps. You go back and refill - 4 steps - and fill bowl 4 - 5 steps. So you take a total of 2 + 2 + 4 + 4 + 5 = 17 steps.

## 9 split strings 

Given a string s with length n, how many ways can you split it into two substrings s_1 and s_2 such that the number of unique characters in s_1 and s_2 are the same?

Parameter
s: A string with length n.
Result
The number of ways you can split it into two substrings that satisfy the condition.
Examples
Example 1:
Input: s = "aaa"

Output: 2

Explanation: It can be split in two ways: "a", "aa" and "aa", "a".

Example 2:
Input: s = "bac"

Output: 0

Explanation: There is no way to split this string into two substrings with equal unique elements.

Constraints

0 <= n <= 10^5
Characters in this string may consist of any alphanumeric character. The characters are case sensitive. That is, same letters with different cases count as different characters.



