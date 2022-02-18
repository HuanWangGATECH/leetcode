'''
Introduction 

Given the weights and profits of ‘N’ items, we are asked to put these items in a knapsack which has a capacity ‘C’. 

The goal is to get the maximum profit out of the items in the knapsack. 

Each item can only be selected once, as we don’t have multiple quantities of any item.

Let’s take the example of Merry, who wants to carry some fruits in the knapsack to get maximum profit. 
   
   Here are the weights and profits of the fruits:

Items: { Apple, Orange, Banana, Melon }

Weights: { 2, 3, 1, 4 }

Profits: { 4, 5, 3, 7 }

Knapsack capacity: 5

Let’s try to put various combinations of fruits in the knapsack, such that their total weight is not more than 5:

Apple + Orange (total weight 5) => 9 profit

Apple + Banana (total weight 3) => 7 profit

Orange + Banana (total weight 4) => 8 profit

Banana + Melon (total weight 5) => 10 profit

This shows that Banana + Melon is the best combination as it gives us the maximum profit and the total weight does not exceed the capacity.
'''



https://leetcode.com/playground/Y9Kg24ag

```python
def knapsack01(profits,weights,capacity):
    
    n=len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0
    dp=[[0 for x in range(capacity+1)] for y in range(n+1)]
    # populate the capacity = 0 columns, with '0' capacity we have '0' profit
    
    
    ##initilization 
    for i in range(0, n+1):
        dp[i][0] = 0   
    #dp[i][j] 0<= i <= n 0<=j <= capacity+1
    for j in range(capacity+1):
        dp[0][j]=0 
    
    
    for i in range(1,n+1):
        for j in range(1,capacity+1):
            
            dp[i][j]=dp[i-1][j]
            if weights[i-1]<=j:
                dp[i][j]=max(dp[i][j],dp[i-1][j-weights[i-1]]+profits[i-1])
    
    
    
    
    
    print (dp)
    
    
    
    return dp[n][capacity]

    
print (knapsack01([1, 6, 10, 16], [1, 2, 3, 5], 7))
print (knapsack01([1, 6, 10, 16], [1, 2, 3, 5], 6))

```


# Equal Subset Sum Partition (medium)


https://leetcode.com/problems/partition-equal-subset-sum/


'''
Problem Statement 

Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both subsets is equal.

Example 1:

Input: {1, 2, 3, 4}

Output: True

Explanation: The given set can be partitioned into two subsets with equal sum: {1, 4} & {2, 3}

Example 2:

Input: {1, 1, 3, 4, 7}

Output: True

Explanation: The given set can be partitioned into two subsets with equal sum: {1, 3, 4} & {1, 7}
'''

