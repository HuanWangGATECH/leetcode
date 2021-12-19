# Here are questions listed in this post 

https://leetcode.com/discuss/interview-question/352460/Google-Online-Assessment-Questions


# 1. Question 1:
Given an Array A, find the minimum amplitude you can get after changing up to 3 elements. Amplitude is the range of the array (basically difference between largest and smallest element).

Example 1:

Input: [-1, 3, -1, 8, 5 4]
Output: 2
Explanation: we can change -1, -1, 8 to 3, 4 or 5

Example 2:

Input: [10, 10, 3, 4, 10]
Output: 0
Explanation: change 3 and 4 to 10

https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/



# 2. Given a string S, we can split S into 2 strings: S1 and S2. Return the number of ways S can be split such that the number of unique characters between S1 and S2 are the same.

Example 1:

Input: "aaaa"
Output: 3
Explanation: we can get a - aaa, aa - aa, aaa- a

Example 2:

Input: "bac"
Output: 0

Example 3:

Input: "ababa"
Output: 2
Explanation: ab - aba, aba - ba

https://leetcode.com/problems/number-of-good-ways-to-split-a-string/

## 3 maximum time 

You are given a string that represents time in the format hh:mm. Some of the digits are blank (represented by ?). Fill in ? such that the time represented by this string is the maximum possible. Maximum time: 23:59, minimum time: 00:00. You can assume that input string is always valid.

Example 1:

Input: "?4:5?"
Output: "14:59"
Example 2:

Input: "23:5?"
Output: "23:59"
Example 3:

Input: "2?:22"
Output: "23:22"
Example 4:

Input: "0?:??"
Output: "09:59"
Example 5:

Input: "??:??"
Output: "23:59"


https://leetcode.com/discuss/interview-question/396769/

## 4 Min Abs Difference of Server Loads

There are some processes that need to be executed. Amount of a load that process causes on a server that runs it, is being represented by a single integer. Total load caused on a server is the sum of the loads of all the processes that run on that server. You have at your disposal two servers, on which mentioned processes can be run. Your goal is to distribute given processes between those two servers in the way that, absolute difference of their loads will be minimized.

Given an array of n integers, of which represents loads caused by successive processes, return the minimum absolute difference of server loads.

Example 1:

Input: [1, 2, 3, 4, 5]
Output: 1
Explanation:
We can distribute the processes with loads [1, 2, 4] to the first server and [3, 5] to the second one,
so that their total loads will be 7 and 8, respectively, and the difference of their loads will be equal to 1.

https://leetcode.com/discuss/interview-question/356433/

## 5 Most Booked Hotel Room 

Given a hotel which has 10 floors [0-9] and each floor has 26 rooms [A-Z]. You are given a sequence of rooms, where + suggests room is booked, - room is freed. You have to find which room is booked maximum number of times.

You may assume that the list describe a correct sequence of bookings in chronological order; that is, only free rooms can be booked and only booked rooms can be freeed. All rooms are initially free. Note that this does not mean that all rooms have to be free at the end. In case, 2 rooms have been booked the same number of times, return the lexographically smaller room.

You may assume:

N (length of input) is an integer within the range [1, 600]
each element of array A is a string consisting of three characters: "+" or "-"; a digit "0"-"9"; and uppercase English letter "A" - "Z"
the sequence is correct. That is every booked room was previously free and every freed room was previously booked.
Example:

Input: ["+1A", "+3E", "-1A", "+4F", "+1A", "-3E"]
Output: "1A"
Explanation: 1A as it has been booked 2 times.


https://leetcode.com/discuss/interview-question/421787/

## 6 Minimum Domino Rotations For Equal Row

https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/


In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

If it cannot be done, return -1.

 

Example 1:


Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
Example 2:

Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row of values equal.


## 7 Time to Type a String

https://leetcode.com/problems/single-row-keyboard (premium)

Imagine you have a special keyboard with all keys in a single row. The layout of characters on a keyboard is denoted by a string keyboard of length 26. Initially your finger is at index 0. To type a character, you have to move your finger to the index of the desired character. The time taken to move your finger from index i to index j is abs(j - i).

Given a string keyboard that describe the keyboard layout and a string text, return an integer denoting the time taken to type string text.

Example 1:

Input: keyboard = "abcdefghijklmnopqrstuvwxy", text = "cba" 
Output: 4
Explanation:
Initially your finger is at index 0. First you have to type 'c'. The time taken to type 'c' will be abs(2 - 0) = 2 because character 'c' is at index 2.
The second character is 'b' and your finger is now at index 2. The time taken to type 'b' will be abs(1 - 2) = 1 because character 'b' is at index 1.
The third character is 'a' and your finger is now at index 1. The time taken to type 'a' will be abs(0 - 1) = 1 because character 'a' is at index 0.
The total time will therefore be 2 + 1 + 1 = 4.
Constraints:

length of keyboard will be equal to 26 and all the lowercase letters will occur exactly once;
the length of text is within the range [1..100,000];
string text contains only lowercase letters [a-z].

## 8 Maximum Level Sum of a Binary Tree

https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

 

Example 1:


Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
Example 2:

Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2


## 9 Google | OA 2019 | Min Number of Chairs

https://leetcode.com/discuss/interview-question/356520

There are n guests who are invited to a party. The k-th guest will attend the party at time S[k] and leave the party at time E[k].

Given an integer array S and an integer array E, both of length n, return an integer denoting the minimum number of chairs you need such that everyone attending the party can sit down.

Example:

Input: S = [1, 2, 6, 5, 3], E = [5, 5, 7, 6, 8]
Output: 3
Explanation:
There are five guests attending the party. 
The 1st guest will arrive at time 1. We need one chair at time 1.
The 2nd guest will arrive at time 2. There are now two guests at the party, so we need two chairs at time 2.
The 5th guest will arrive at time 3. There are now three guests at the party, so we need three chairs at time 3.
The 4th guest will arrive at time 5 and, at the same moment, the 1st and 2nd guests will leave the party.
There are now two (the 4th and 5th) guests at the party, so we need two chairs at time 5.
The 3rd guest will arrive at time 6, and the 4th guest will leave the party at the same time.
There are now two (the 3rd and 5th) guests at the party, so we need two chairs at time 6. 
So we need at least 3 chairs.
Related problems:

https://leetcode.com/problems/meeting-rooms-ii (premium)

## 10 K Closest Points to Origin

https://leetcode.com/problems/k-closest-points-to-origin/

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

 

Example 1:


Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
 

Constraints:

1 <= k <= points.length <= 104
-104 < xi, yi < 104

## 11 Odd Even Jump 

https://leetcode.com/problems/odd-even-jump/


You are given an integer array arr. From some starting index, you can make a series of jumps. The (1st, 3rd, 5th, ...) jumps in the series are called odd-numbered jumps, and the (2nd, 4th, 6th, ...) jumps in the series are called even-numbered jumps. Note that the jumps are numbered, not the indices.

You may jump forward from index i to index j (with i < j) in the following way:

During odd-numbered jumps (i.e., jumps 1, 3, 5, ...), you jump to the index j such that arr[i] <= arr[j] and arr[j] is the smallest possible value. If there are multiple such indices j, you can only jump to the smallest such index j.
During even-numbered jumps (i.e., jumps 2, 4, 6, ...), you jump to the index j such that arr[i] >= arr[j] and arr[j] is the largest possible value. If there are multiple such indices j, you can only jump to the smallest such index j.
It may be the case that for some index i, there are no legal jumps.
A starting index is good if, starting from that index, you can reach the end of the array (index arr.length - 1) by jumping some number of times (possibly 0 or more than once).

Return the number of good starting indices.

 

Example 1:

Input: arr = [10,13,12,14,15]
Output: 2
Explanation: 
From starting index i = 0, we can make our 1st jump to i = 2 (since arr[2] is the smallest among arr[1], arr[2], arr[3], arr[4] that is greater or equal to arr[0]), then we cannot jump any more.
From starting index i = 1 and i = 2, we can make our 1st jump to i = 3, then we cannot jump any more.
From starting index i = 3, we can make our 1st jump to i = 4, so we have reached the end.
From starting index i = 4, we have reached the end already.
In total, there are 2 different starting indices i = 3 and i = 4, where we can reach the end with some number of
jumps.
Example 2:

Input: arr = [2,3,1,1,4]
Output: 3
Explanation: 
From starting index i = 0, we make jumps to i = 1, i = 2, i = 3:
During our 1st jump (odd-numbered), we first jump to i = 1 because arr[1] is the smallest value in [arr[1], arr[2], arr[3], arr[4]] that is greater than or equal to arr[0].
During our 2nd jump (even-numbered), we jump from i = 1 to i = 2 because arr[2] is the largest value in [arr[2], arr[3], arr[4]] that is less than or equal to arr[1]. arr[3] is also the largest value, but 2 is a smaller index, so we can only jump to i = 2 and not i = 3
During our 3rd jump (odd-numbered), we jump from i = 2 to i = 3 because arr[3] is the smallest value in [arr[3], arr[4]] that is greater than or equal to arr[2].
We can't jump from i = 3 to i = 4, so the starting index i = 0 is not good.
In a similar manner, we can deduce that:
From starting index i = 1, we jump to i = 4, so we reach the end.
From starting index i = 2, we jump to i = 3, and then we can't jump anymore.
From starting index i = 3, we jump to i = 4, so we reach the end.
From starting index i = 4, we are already at the end.
In total, there are 3 different starting indices i = 1, i = 3, and i = 4, where we can reach the end with some
number of jumps.
Example 3:

Input: arr = [5,1,3,4,2]
Output: 3
Explanation: We can reach the end from starting indices 1, 2, and 4.
 

Constraints:

1 <= arr.length <= 2 * 104
0 <= arr[i] < 105

## 12 License Key Formatting

https://leetcode.com/problems/license-key-formatting/

You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.

We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

Return the reformatted license key.

 

Example 1:

Input: s = "5F3Z-2e-9-w", k = 4
Output: "5F3Z-2E9W"
Explanation: The string s has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.
Example 2:

Input: s = "2-5g-3-J", k = 2
Output: "2-5G-3J"
Explanation: The string s has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.
 

Constraints:

1 <= s.length <= 105
s consists of English letters, digits, and dashes '-'.
1 <= k <= 104

## 13 Unique Email Addresses

https://leetcode.com/problems/unique-email-addresses/

Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.

For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.

For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.

For example, "m.y+name@email.com" will be forwarded to "my@email.com".
It is possible to use both of these rules at the same time.

Given an array of strings emails where we send one email to each emails[i], return the number of different addresses that actually receive mails.

 

Example 1:

Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.
Example 2:

Input: emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
Output: 3
 

Constraints:

1 <= emails.length <= 100
1 <= emails[i].length <= 100
emails[i] consist of lowercase English letters, '+', '.' and '@'.
Each emails[i] contains exactly one '@' character.
All local and domain names are non-empty.
Local names do not start with a '+' character.

## 14 Fruits in to baskets 

https://leetcode.com/problems/fruit-into-baskets/

You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

 

Example 1:

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.
Example 2:

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].
Example 3:

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].
Example 4:

Input: fruits = [3,3,3,1,2,1,1,2,3,3,4]
Output: 5
Explanation: We can pick from trees [1,2,1,1,2].
 

Constraints:

1 <= fruits.length <= 105
0 <= fruits[i] < fruits.length

## 15 Min Days to Bloom
https://leetcode.com/discuss/interview-question/334191

Given an array of roses. roses[i] means rose i will bloom on day roses[i]. Also given an int k, which is the minimum number of adjacent bloom roses required for a bouquet, and an int n, which is the number of bouquets we need. Return the earliest day that we can get n bouquets of roses.

Example:
Input: roses = [1, 2, 4, 9, 3, 4, 1], k = 2, n = 2
Output: 4
Explanation:
day 1: [b, n, n, n, n, n, b]
The first and the last rose bloom.

day 2: [b, b, n, n, n, n, b]
The second rose blooms. Here the first two bloom roses make a bouquet.

day 3: [b, b, n, n, b, n, b]

day 4: [b, b, b, n, b, b, b]
Here the last three bloom roses make a bouquet, meeting the required n = 2 bouquets of bloom roses. So return day 4.

int minDaysBloom(int[] roses, int k, int n) {
}

## 16 Fill Matrix
https://leetcode.com/discuss/interview-question/341295/Google-or-Online-Assessment-2019-or-Fill-Matrix

Given a NxN matrix. Fill the integers from 1 to n*n to this matrix that makes the sum of each row, each column and the two diagonals equal.

Example 1:

Input: n = 2
Output: null
Explanation: We need to fill [1, 2, 3, 4] into a 2x2 matrix, which is not possible so return null.
Example 2:

Input: n = 3
Output:
[[8, 3, 4],
 [1, 5, 9],
 [6, 7, 2]]
Explanation: We need to fill [1, 2, 3... 9] into a 3x3 matrix. This is one way to do it
Each row [8, 3, 4] [1, 5, 9] [6, 7, 2] sum is 15.
Each column [8, 1, 6] [3, 5, 7] [4, 9, 2] sum is 15.
The two diagonals [8, 5, 2] [4, 5, 6] sum is 15.
int[][] fillMatrix(int n) {
}


## 17 Decreasing Subsequences

https://leetcode.com/discuss/interview-question/350233/Google-or-Summer-Intern-OA-2019-or-Decreasing-Subsequences

Given an int array nums of length n. Split it into strictly decreasing subsequences. Output the min number of subsequences you can get by splitting.

Example 1:

Input: [5, 2, 4, 3, 1, 6]
Output: 3
Explanation:
You can split this array into: [5, 2, 1], [4, 3], [6]. And there are 3 subsequences you get.
Or you can split it into [5, 4, 3], [2, 1], [6]. Also 3 subsequences.
But [5, 4, 3, 2, 1], [6] is not legal because [5, 4, 3, 2, 1] is not a subsuquence of the original array.
Example 2:

Input: [2, 9, 12, 13, 4, 7, 6, 5, 10]
Output: 4
Explanation: [2], [9, 4], [12, 10], [13, 7, 6, 5]
Example 3:

Input: [1, 1, 1]
Output: 3
Explanation: Because of the strictly descending order you have to split it into 3 subsequences: [1], [1], [1]
Challenge
Solution
Related problems

## 18  Max Distance

https://leetcode.com/discuss/interview-question/350363/Google-or-OA-2018-or-Max-Distance

The distance between 2 binary strings is the sum of their lengths after removing the common prefix. For example: the common prefix of 1011000 and 1011110 is 1011 so the distance is len("000") + len("110") = 3 + 3 = 6.

Given a list of binary strings, pick a pair that gives you maximum distance among all possible pair and return that distance.

## 19 Stores and Houses
https://leetcode.com/discuss/interview-question/350363/Google-or-OA-2018-or-Max-Distance


You are given 2 arrays representing integer locations of stores and houses (each location in this problem is one-dementional). For each house, find the store closest to it.
Return an integer array result where result[i] should denote the location of the store closest to the i-th house. If many stores are equidistant from a particular house, choose the store with the smallest numerical location. Note that there may be multiple stores and houses at the same location.

Example 1:

Input: houses = [5, 10, 17], stores = [1, 5, 20, 11, 16]
Output: [5, 11, 16]
Explanation: 
The closest store to the house at location 5 is the store at the same location.
The closest store to the house at location 10 is the store at the location 11.
The closest store to the house at location 17 is the store at the location 16.
Example 2:

Input: houses = [2, 4, 2], stores = [5, 1, 2, 3]
Output: [2, 3, 2]
Example 3:

Input: houses = [4, 8, 1, 1], stores = [5, 3, 1, 2, 6]
Output: [3, 6, 1, 1]

