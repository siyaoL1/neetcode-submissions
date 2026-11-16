class Solution:
    def myPow(self, x: float, n: int) -> float:
        memo = {1: x}
        negative = False
        if n < 0:
            negative = True
            n *= -1
        def helper(n):
            if n == 0:
                return 1
            if n in memo:
                return memo[n]
            half = helper(n // 2)
            result = half * half
            if n % 2:
                result *= helper(1)
            memo[n] = result
            return result
        result = helper(n)
        if negative:
            result = 1/result
        return result
