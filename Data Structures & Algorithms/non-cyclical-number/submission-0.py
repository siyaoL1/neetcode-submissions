class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n not in seen:
            seen.add(n)
            digits = []
            while n:
                digits.append(n % 10)
                n = n // 10
            curr_sum = 0
            for digit in digits:
                curr_sum += digit * digit
            if curr_sum == 1:
                return True
            n = curr_sum

        return False