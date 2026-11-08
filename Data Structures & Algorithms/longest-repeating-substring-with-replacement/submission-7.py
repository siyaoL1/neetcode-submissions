class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        left, right = 0, 0
        max_result = -1
        for right in range(len(s)):
            char = s[right]
            counts[char] = 1 + counts.get(char, 0)

            max_freq = max(counts.values())

            while right - left + 1 - max_freq > k:
                counts[s[left]] -= 1
                left += 1

            max_result = max(max_result, right - left + 1)
                
        return max_result