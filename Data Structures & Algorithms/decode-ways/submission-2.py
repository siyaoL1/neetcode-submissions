class Solution:
    def numDecodings(self, s: str) -> int:
        map = set(f"{i}" for i in range(1, 27))
        memo = {}

        def ways(i):
            if i == len(s):
                return 1
            if i == len(s) - 1:
                return 1 if s[i] in map else 0
            
            if i in memo:
                return memo[i]
            
            result = 0
            if s[i:i + 1] in map:
                remaining = ways(i+1)
                if remaining != -1:
                    result += remaining
            
            if s[i:i + 2] in map:
                remaining = ways(i+2)
                if remaining != -1:
                    result += remaining
            memo[i] = result
            return result

        return ways(0)
            
            
            
            