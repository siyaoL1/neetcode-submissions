class Solution:
    def numDecodings(self, s: str) -> int:
        map = set(f"{i}" for i in range(1, 27))
        memo = {}

        def ways(i):
            if i == len(s):
                return 1
            if i in memo:
                return memo[i]
            
            result = 0
            if s[i] in map:
                result += ways(i + 1)
            
            if i + 1 < len(s) and s[i:i + 2] in map:
                result += ways(i + 2)
            
            memo[i] = result
            return result

        return ways(0)
            
            
            
            