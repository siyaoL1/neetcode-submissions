class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # we can have two pointer the right pointer moves forward when there's no repleating char
        # if we see one repeating char move the left pointer to the right of the first appearance
        if not s:
            return 0
        seen = {}

        left, right = 0, 0
        max_len = 1

        while right < len(s):
            # print(left, right, max_len, seen)
            if left == right:
                seen[s[left]] = left
            elif s[right] in seen and seen[s[right]] >= left:
                left = seen[s[right]] + 1
                seen[s[right]] = right    
            else:
                seen[s[right]] = right

            right += 1
            max_len = max(max_len, right - left)
            
            
        return max_len