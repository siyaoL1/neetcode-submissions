class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev_one, prev_two = 0, 0

        for stair in range(len(cost)):
            curr = min(prev_one, prev_two) + cost[stair]
            prev_two = prev_one
            prev_one = curr
        

        return min(prev_two, prev_one)
        