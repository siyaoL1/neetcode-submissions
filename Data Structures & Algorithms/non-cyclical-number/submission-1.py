class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            digits = []
            square_sum = 0
            while n:
                n, digit = divmod(n, 10)
                square_sum += digit * digit
            n = square_sum

        return n == 1