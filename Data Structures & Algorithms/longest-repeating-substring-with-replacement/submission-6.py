class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        counts = {}
        left = 0
        right = 0
        max_result = -1
        while right < len(s):
            char = s[right]
            counts[char] = counts.get(char, 0) + 1

            # Highest frequency in the current window
            max_freq = max(counts.values(), default=0)

            curr_size = right - left + 1
            if curr_size - max_freq <= k:
                max_result = max(max_result, curr_size)
            else:
                # When a character leaves the window
                counts[s[left]] -= 1
                left += 1
            right += 1
        return max_result