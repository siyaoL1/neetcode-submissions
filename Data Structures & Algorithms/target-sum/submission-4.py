from collections import defaultdict


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ways_by_sum = {0: 1}

        for num in nums:
            next_ways = defaultdict(int)
            for total, ways in ways_by_sum.items():
                next_ways[total + num] += ways
                next_ways[total - num] += ways
            ways_by_sum = next_ways

        return ways_by_sum.get(target, 0)