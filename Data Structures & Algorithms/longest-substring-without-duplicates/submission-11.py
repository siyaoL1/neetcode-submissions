class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Maintain left and right pointer sliding window
        # Keep a visited dict that stores the character and the index of it
        # When we see one character already in our visited dict and in the current left right range
        # updated the index and update left to be current index
        left, right = 0, 0
        visited = {}
        length = len(s)
        max_len = 0
        
        for right in range(length):
            curr_char = s[right]
            if curr_char in visited and left <= visited[curr_char]:
                left = visited[curr_char] + 1
            visited[curr_char] = right
            max_len = max(max_len, right - left + 1)
        
        return max_len
