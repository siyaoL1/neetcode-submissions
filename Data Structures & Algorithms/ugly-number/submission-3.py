class Solution:
    def isUgly(self, n: int) -> bool:        
        for prime in [2, 3, 5]:
            while n % prime == 0:
                n = n / prime

        return n == 1