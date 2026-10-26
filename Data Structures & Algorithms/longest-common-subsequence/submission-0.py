class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1_len = len(text1)
        text2_len = len(text2)
        history = {}

        def helper(i, j):
            if i >= text1_len or j >= text2_len:
                return 0
            
            if (i, j) in history:
                return history[(i, j)]

            results = [
                helper(i, j + 1),
                helper(i + 1, j)
            ]
            if text1[i] == text2[j]:
                results.append(1 + helper(i + 1, j + 1))
            else:
                results.append(helper(i + 1, j + 1))
            
            max_result = max(results)
            history[(i, j)] = max_result
            return max_result
        return helper(0, 0)
