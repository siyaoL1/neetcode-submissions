class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = [0]
        for curr_amount in range(1, amount + 1):
            min_coins = math.inf
            for coin in coins:
                prev_amount = curr_amount - coin
                if prev_amount >= 0 and dp[prev_amount] >= 0:
                    min_coins = min(min_coins, dp[prev_amount] + 1)
            if min_coins != math.inf:
                dp.append(min_coins)
            else:
                dp.append(-1)
        
        return dp[amount]

test_cases = [
    ([1, 2], 3, 2), # reachable
    ([1], 0, 0), # edge case
    ([3, 5], 4, -1), # not reachable
    ([5, 1], 4, 4), # reachable but if choose larger value immediately not reachable
    ([5, 2], 6, 3)
]


solution = Solution()

for coins, amount, expected in test_cases:
    result = solution.coinChange(coins, amount)
    assert result == expected, f"FAILED coins:{coins}, amount:{amount}, result:{result}, expected:{expected}"