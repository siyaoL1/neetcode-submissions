class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        def helper(n):
            if n == 0:
                return 1.0

            half = helper(n // 2)
            result = half * half

            if n % 2:
                result *= x

            return result

        return helper(n)