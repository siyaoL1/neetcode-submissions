class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
            
        seen = {}
        left = 0
        max_len = 0
        for right in range(len(s)):
            c = s[right]
            if c in seen and seen[c] >= left:
                left = seen[c] + 1
            seen[c] = right
            max_len = max(max_len, right - left + 1)
        
        return max_len