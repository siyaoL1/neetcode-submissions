class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev_two, prev_one = 1, 2

        for i in range(3, n + 1):
            curr = prev_one + prev_two
            prev_two = prev_one
            prev_one = curr
        
        return prev_one