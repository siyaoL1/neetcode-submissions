class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [0] * (n + 1)

        for i in range(m - 1, -1, -1):
            curr_dp = [0] * (n + 1)
            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:
                    curr_dp[j] = 1 + dp[j + 1]
                else:
                    curr_dp[j] = max(dp[j], curr_dp[j + 1])
            dp = curr_dp
        
        return dp[0]
