from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1

        for num in nums:
            curr_sums = defaultdict(int)
            for curr_num in (num, -num):
                for existing_sum, times in dp.items():
                    curr_sums[existing_sum + curr_num] += times
            dp = curr_sums

        return dp.get(target, 0)