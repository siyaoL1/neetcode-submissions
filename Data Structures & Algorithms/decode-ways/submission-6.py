class Solution:
    def numDecodings(self, s: str) -> int:
        one_ahead = 1
        two_ahead = 0
        valid_codes = {str(number) for number in range(1, 27)}
        n = len(s)
        
        for i in range(n - 1, -1, -1):
            current = 0
            if s[i] in valid_codes:
                current += one_ahead
            
            if i + 1 < n and s[i : i + 2] in valid_codes:
                current += two_ahead

            one_ahead, two_ahead = current, one_ahead
        
        return one_ahead
            
            
            
            