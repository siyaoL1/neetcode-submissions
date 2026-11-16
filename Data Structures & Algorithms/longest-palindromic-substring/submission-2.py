class Solution:
    def longestPalindrome(self, s: str) -> str:
        best_left = best_right = 0

        for center in range(len(s)):
            for left, right in ((center, center), (center, center + 1)):
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    if right - left > best_right - best_left:
                        best_left, best_right = left, right

                    left -= 1
                    right += 1

        return s[best_left:best_right + 1]