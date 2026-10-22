class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry_over = 1
        result = []
        for n in range(len(digits) - 1, -1, -1):
            curr_digit = digits[n] + carry_over
            carry_over = 0
            if curr_digit == 10:
                carry_over = 1
                result.append(0)
            else:
                result.append(curr_digit)
        
        if carry_over:
            result.append(1)
        result.reverse()

        return result