class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        seen = {}
        left = 0

        for right in range(len(s)):
            curr = s[right]
            if curr in seen and seen[curr] >= left:
                left = seen[curr] + 1
            seen[curr] = right
            result = max(result, right - left + 1)

        return result


