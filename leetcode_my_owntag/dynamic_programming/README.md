# leetcode dynamic programming question list 
https://leetcode.com/tag/dynamic-programming/

# educative questions 
https://www.educative.io/courses/dynamic-programming-in-python



# Patterns in DP
There are 5 commong patterns of DP according to Educative course https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/RM1BDv71V60

## Pattern 1: Knapsack 0/1 
## Pattern 2: Knapsack unbounded 
## Pattern 3: Fibonacci number 
## Pattern 4: Palindromic subsequence 
## Pattern 5: Longest common substring 


# 322 Coin change 
https://leetcode.com/problems/coin-change/


```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp=[math.inf]*(amount+1)
        
        dp[0]=0
      
        for i in range(1,amount+1):
            
            for coin in coins:
                if i>=coin:
                    dp[i]=min(dp[i-coin]+1,dp[i])
        
        
        #print (dp)
        return dp[amount] if dp[amount]!=math.inf else -1
```


==Greedy approach doesn't go well with this question. Take this example. coins = [100, 90, 1] amount = 385
The greedy answer will be [3 * 100, 1 * 85], so all together 88
But a better combination will be [2 * 100, 2 * 90, 5 * 1], so 9.. hope you got the idea==






# 2224. Minimum Number of Operations to Convert Time
https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/


You are given two strings current and correct representing two 24-hour times.

24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59. The earliest 24-hour time is 00:00, and the latest is 23:59.

In one operation you can increase the time current by 1, 5, 15, or 60 minutes. You can perform this operation any number of times.

Return the minimum number of operations needed to convert current to correct.

 

Example 1:

Input: current = "02:30", correct = "04:35"
Output: 3
Explanation:
We can convert current to correct in 3 operations as follows:
- Add 60 minutes to current. current becomes "03:30".
- Add 60 minutes to current. current becomes "04:30".
- Add 5 minutes to current. current becomes "04:35".
It can be proven that it is not possible to convert current to correct in fewer than 3 operations.
Example 2:

Input: current = "11:00", correct = "11:01"
Output: 1
Explanation: We only have to add one minute to current, so the minimum number of operations needed is 1.


```python 
class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        current_time = 60 * int(current[0:2]) + int(current[3:5]) # Current time in minutes
        target_time = 60 * int(correct[0:2]) + int(correct[3:5]) # Current time in minutes
        diff = target_time - current_time # Difference b/w current and target times in minutes
        count = 0 # Required number of operations
		# Use GREEDY APPROACH to calculate number of operations
        for i in [60, 15, 5, 1]:
            count += diff // i # add number of operations needed with i to count
            diff %= i # Diff becomes modulo of diff with i
        return count
```
