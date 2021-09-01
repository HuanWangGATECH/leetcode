class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        mini = prices[0]
        for i in range(1,len(prices)):
            prof = max(prices[i]-mini,prof)
            mini = min(prices[i],mini)
        return prof
