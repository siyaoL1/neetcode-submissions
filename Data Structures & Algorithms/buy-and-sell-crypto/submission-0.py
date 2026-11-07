class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for l in range(len(prices)):
            for r in range(len(prices)-1, l, -1):
                max_profit = max(max_profit, prices[r] - prices[l])

        return max_profit